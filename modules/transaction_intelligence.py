import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("ETHERSCAN_API_KEY")


def get_transaction_intelligence(address):

    url = (
        f"https://api.etherscan.io/v2/api"
        f"?chainid=1"
        f"&module=account"
        f"&action=txlist"
        f"&address={address}"
        f"&startblock=0"
        f"&endblock=99999999"
        f"&sort=desc"
        f"&apikey={API_KEY}"
    )

    try:

        response = requests.get(url, timeout=20)

        data = response.json()

        if data.get("status") != "1":

            return None

        txs = data["result"]

        total_tx = len(txs)

        incoming = 0
        outgoing = 0

        total_received = 0
        total_sent = 0
        recent_transactions = []

        for tx in txs:

            value = int(tx["value"]) / 1000000000000000000

            if tx["to"].lower() == address.lower():

                incoming += 1
                total_received += value

            elif tx["from"].lower() == address.lower():

                outgoing += 1
                total_sent += value
            
            if len(recent_transactions) < 5:

                recent_transactions.append({

                    "hash": tx["hash"][:18] + "...",

                    "value": round(value, 4),

                    "date": datetime.fromtimestamp(
                        int(tx["timeStamp"])
                     ).strftime("%d-%m-%Y")

                })

        first_activity = datetime.fromtimestamp(
            int(txs[-1]["timeStamp"])
        ).strftime("%d-%m-%Y")

        last_activity = datetime.fromtimestamp(
            int(txs[0]["timeStamp"])
        ).strftime("%d-%m-%Y")

        if total_tx > 0:

            first_activity = txs[-1]["timeStamp"]
            last_activity = txs[0]["timeStamp"]
            first_date = datetime.fromtimestamp(
		int(txs[-1]["timeStamp"])
	    )
        wallet_age = (
    	    datetime.now() - first_date
	).days

        return {

    	    "total_tx": total_tx,

    	    "incoming": incoming,

    	    "outgoing": outgoing,

    	    "received": round(total_received, 4),

    	    "sent": round(total_sent, 4),

            "first_activity": first_activity,

    	    "last_activity": last_activity,

    	    "wallet_age": wallet_age,

    	    "recent_transactions": recent_transactions

	}

    except Exception as e:

        print(f"[ERROR] {e}")

        return None
