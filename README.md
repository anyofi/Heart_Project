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
   - Пример структуры файла `heart_test.csv`:
     ```csv
     age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
     52,1,0,125,212,0,1,168,0,1.0,2,2,3
     43,0,1,130,204,0,0,155,0,3.5,1,0,2
     ```

5. Нажмите **Execute**
   
6. Получите результат в формате JSON


