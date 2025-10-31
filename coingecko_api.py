import requests # pyright: ignore[reportMissingModuleSource]
import time



def fetch_prices(tokens):
    ids = ",".join(tokens)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            print(" Rate limit hit. Backing off for 60 seconds...")
            time.sleep(60)  
            return {}
        else: 
            print(f" API error {response.status_code}")
    except requests.exceptions.Timeout:
        print(" Request timed out. Skipping this cycle.")
    except requests.exceptions.RequestException as e:
        print(f" Request failed: {e}")
    except KeyboardInterrupt:
        print("Interrupted by user. Exiting gracefully.")
        exit()

    return {}