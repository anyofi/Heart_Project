# Heart Disease Prediction Project

Проект для предсказания риска сердечных заболеваний с использованием FastAPI и машинного обучения.

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/anyofi/heart_project.git
cd heart_project
```

2. Создайте виртуальное окружение:
```bash
python -m venv fastapi_env
```

3. Активируйте окружение:
```
# Windows (cmd):
fastapi_env\Scripts\activate
# Linux/MacOS:
source fastapi_env/bin/activate
```

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Запуск
Локальный запуск:
``` bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
После запуска приложение будет доступно:

1. API: http://localhost:8000/

2. Документация: http://localhost:8000/docs

## Структура проекта

- `app/` - исходный код FastAPI приложения
- `data/` - данные для обучения и тестирования
- `trained_models/` - обученные модели машинного обучения
- `research.ipynb` - Jupyter notebook с исследованиями
- `requirements.txt` - зависимости Python

## API Endpoints

- `GET /` - основная страница
- `POST /api/batch_predict` - получение предсказаний для CSV файла

## Примеры запросов

1. Откройте документацию API:  
   http://localhost:8000/docs

2. Найдите эндпоинт `POST /batch_predict`  

3. Нажмите **Try it out** → **Choose File**  

4. Загрузите CSV-файл с данными пациентов  
   - Обязательные поля файла `heart_test.csv`:
     ```csv
    Age,Cholesterol,Heart rate,Diabetes,Family History,Smoking,Obesity,
    Alcohol Consumption,Exercise Hours Per Week,Diet,Previous Heart Problems,
    Medication Use,Stress Level,Sedentary Hours Per Day,Income,BMI,Triglycerides,
    Physical Activity Days Per Week,Sleep Hours Per Day,Blood sugar,CK-MB,Troponin,
    Gender,Systolic blood pressure,Diastolic blood pressure,id
     ```

5. Нажмите **Execute**
   
6. Получите результат в формате JSON


