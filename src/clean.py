import pandas as pd


def clean_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df.drop_duplicates()
    df = df.dropna()
    return df
