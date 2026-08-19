import requests
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("P5MJI28EGD2GWPXFCZS2GZZEV4QQ26Q48Q")


def get_transactions(address):

    url = (
        "https://api.etherscan.io/api"
        f"?module=account"
        f"&action=txlist"
        f"&address={address}"
        f"&startblock=0"
        f"&endblock=99999999"
        f"&page=1"
        f"&offset=20"
        f"&sort=desc"
        f"&apikey={API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    return data
