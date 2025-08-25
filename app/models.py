import joblib
import pandas as pd
from typing import List

class HeartDiseaseModel:
    def __init__(self):
        self.is_loaded = False
        try:
            self.model = joblib.load("trained_models/best_model_20250823_182438.joblib")
            self.is_loaded = True
        except Exception as e:
            raise Exception(f"Ошибка загрузки модели: {str(e)}")

    def predict(self, data: pd.DataFrame) -> List[float]:
        if not self.is_loaded:
            raise Exception("Модель не загружена")

        # возвращаем вероятности для всех строк
        probabilities = self.model.predict_proba(data)[:, 1]
        return probabilities.tolist()  # преобразуем в список