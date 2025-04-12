import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()
login_senha = os.getenv("loginsenha")

url = "https://lit.stays.com.br"
endpoint = "/external/v1/booking/reservations-export"

querystring = {"from": "2024-12-10", "to": "2024-12-10", "dateType": "creation"}

def extract_response(url,endpoint,querystring):
    headers = {
        "Authorization": f"Basic {login_senha}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(url + endpoint, headers=headers, data=json.dumps(querystring))
    dados = response.json()
    
    return dados

if __name__ == "__main__":
    reservas = extract_response(url,endpoint,querystring)[0]
    for reserva in reservas:
        print(reserva['listing']['internalName'])