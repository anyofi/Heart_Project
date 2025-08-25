# Heart Disease Prediction Project

Проект для предсказания риска сердечных заболеваний с использованием FastAPI и машинного обучения.

## Установка и запуск

1. Активируйте виртуальное окружение:

``` bash
fastapi_env\Scripts\activate
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Запустите приложение:

```bush
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

4. Откройте в браузере: http://localhost:8000/docs

## Структура проекта

- `app/` - исходный код FastAPI приложения
- `data/` - данные для обучения и тестирования
- `trained_models/` - обученные модели машинного обучения
- `research.ipynb` - Jupyter notebook с исследованиями
- `requirements.txt` - зависимости Python

## API Endpoints

- `GET /` - основная страница
- `POST /api/batch_predict` - получение предсказаний для CSV файла