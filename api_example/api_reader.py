import requests
import pandas as pd

def fetch_quote():
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame([data[0]])
        df = df[['q', 'a']].rename(columns={'q': 'Цитата', 'a': 'Автор'})
        return df
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

if __name__ == "__main__":
    df = fetch_quote()
    if df is not None:
        print(df.to_string(index=False, header=False))
    else:
        print("Не удалось загрузить")