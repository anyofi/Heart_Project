import pandas as pd

# функция предобработки данных
def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    # удаление ненужных колонок
    df_clean = df.drop(
        columns=[
            'Unnamed: 0', 'Income', 'CK-MB', 'Troponin',
            'blood_sugar', 'smoking', 'ck_mb', 'troponin'
        ],
        errors='ignore'
    )

    # приведение названий колонок к snake_case
    df_clean.columns = [
        col.strip().lower().replace(' ', '_')
        for col in df_clean.columns
    ]

    # удаление строк с diet=3
    df_clean = df_clean[df_clean['diet'] != 3]

    # обработка gender
    gender_mapping = {'Male': 1, 'Female': 0}
    df_clean['gender'] = df_clean['gender'].map(gender_mapping)

    return df_clean
