import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ETHERSCAN_API_KEY")

def get_eth_balance(address):
    url = (
        f"https://api.etherscan.io/v2/api"
    	f"?chainid=1"
    	f"&module=account"
    	f"&action=balance"
    	f"&address={address}"
    	f"&tag=latest"
    	f"&apikey={API_KEY}"
     )

    try:
        response = requests.get(url, timeout=10)

        data = response.json()

        if data.get("status") == "1":

            wei = int(data["result"])

            eth = wei / 1000000000000000000

            return round(eth, 6)

        else:

            print(f"[ERROR] {data}")

            return None

    except Exception as e:

        print(f"[ERROR] {e}")

        return None
