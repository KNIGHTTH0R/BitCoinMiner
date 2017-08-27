import requests
import json
import time


def getLatestBlockTemplate():
    reqbody = {
        "method": "getblocktemplate",
        "params": [
            {
                "capabilities": [
                    "coinbasetxn",
                    "coinbasevalue"
                ],
                "mode":"template"
            }
        ],
        "id": "0"
    }
    headers = {"Content-Type": "text/plain"}
    r = requests.post(
        "http://localhost:8332",
        data=json.dumps(reqbody),
        headers=headers,
        auth=('ivegot', 'thenuts')
    )
    response = r.json()
    return response["result"]


def main():
    response = getLatestBlockTemplate()
    transactions = response["transactions"]


if __name__ == '__main__':
    main()
