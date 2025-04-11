import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()
login_senha = os.getenv("loginsenha")

url = "https://lit.stays.com.br"
endpoint = "/external/v1/booking/reservations-export"

querystring = {"from": "2024-12-10", "to": "2024-12-12", "dateType": "creation"}

headers = {
    "Authorization": f"Basic {login_senha}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.post(url + endpoint, headers=headers, data=json.dumps(querystring))
dados = response.json()

print(dados)

