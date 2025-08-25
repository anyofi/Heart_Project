from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from typing import List, Dict
import pandas as pd
from app.models import HeartDiseaseModel
from app.schemas import HeartProjectInput
from app.preprocessing import preprocess_data  # Добавляем импорт предобработки

app = FastAPI(title="Heart Disease Prediction API")

# загружаем модель
model = HeartDiseaseModel()

@app.post("/api/batch_predict")
async def predict_batch(file: UploadFile = File(...)):
    try:
        # читаем CSV
        df = pd.read_csv(file.file)

        # применяем предобработку
        df_processed = preprocess_data(df)

        ids = df_processed.pop('id').tolist()  # сохраняем id

        # Делаем предсказания для всего датасета
        risks = model.predict(df_processed)

        # результат с оригинальными id
        predictions = [
            {"id": str(id_), "risk": round(float(risk) * 100, 1)}  # Умножаем на 100 для процентов
            for id_, risk in zip(ids, risks)
        ]

        return {"predictions": predictions}

    except ValidationError as ve:
        return JSONResponse(content={"error": ve.errors()}, status_code=422)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.get("/")
def home():
    return {"message": "API для предсказания сердечных заболеваний"}