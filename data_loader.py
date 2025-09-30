import pandas as pd

FILE_ID = "1j7ZAFLYStESJoCrkH0-bLctoxV75djUf"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

print("Загрузка данных...")
raw_data = pd.read_csv(file_url)

data = raw_data.astype({
    "Customer_ID": "string",
    "Product_ID": "string",
    "Transaction_ID": "string",
    "Purchase_Frequency": "int64",
    "Average_Order_Value": "float64",
    "Most_Frequent_Category": "category",
    "Time_Between_Purchases": "int64",
    "Region": "category",
    "Churn_Probability": "float64",
    "Lifetime_Value": "float64",
    "Season": "category",
    "Preferred_Purchase_Times": "category",
    "Retention_Strategy": "category"
})

data["Launch_Date"] = pd.to_datetime(data["Launch_Date"])
data["Peak_Sales_Date"] = pd.to_datetime(data["Peak_Sales_Date"])

print(data.info())

output_file = "data.parquet"
data.to_parquet(output_file, index=False)

print(f"\nФайл сохранён: {output_file}")
