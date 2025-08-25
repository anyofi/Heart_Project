from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'

class HeartProjectInput(BaseModel):
    diabetes: bool
    family_history: bool
    obesity: bool
    alcohol_consumption: bool
    previous_heart_problems: bool
    medication_use: bool
    diet: int
    stress_level: int
    physical_activity_days_per_week: int
    age: float
    cholesterol: float
    heart_rate: float
    exercise_hours_per_week: float
    sedentary_hours_per_day: float
    bmi: float
    triglycerides: float
    sleep_hours_per_day: float
    blood_sugar: float
    ck_mb: float
    troponin: float
    systolic_blood_pressure: float
    diastolic_blood_pressure: float
    gender: Gender
