import os
from src.clean import clean_csv
from src.upload import upload_to_s3

CSV_PATH = "data/sample.csv"
PARQUET_PATH = "output/data.parquet"

BUCKET = "rg-test300"
KEY = "parquet/data.parquet"

# ✅ CREATE output/ DIRECTORY IN CI
os.makedirs("output", exist_ok=True)

df = clean_csv(CSV_PATH)
df.to_parquet(PARQUET_PATH)

upload_to_s3(PARQUET_PATH, BUCKET, KEY)
