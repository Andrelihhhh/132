import requests
import pandas as pd
import time

def fetch_quotes(n=5):
    url = "https://zenquotes.io/api/random"
    quotes = []

    for i in range(n):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()[0]
            quotes.append({"quote": data["q"], "author": data["a"]})
        except Exception as e:
            print(f"{i+1}. Ошибка: {e}")
        time.sleep(1)

    df = pd.DataFrame(quotes)
    return df


if __name__ == "__main__":
    df = fetch_quotes(5)
    print(df.head())

    output_file = "quotes.csv"
    df.to_csv(output_file, index=False)
