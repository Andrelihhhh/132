import pandas as pd

FILE_ID = "1j7ZAFLYStESJoCrkH0-bLctoxV75djUf"

file_url = f"https://drive.google.com/uc?id={FILE_ID}"

print("Загрузка данных...")
raw_data = pd.read_csv(file_url)

print("\nПервые 10 строк датасета:")
print(raw_data.head(10))