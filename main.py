import os
import requests
from dotenv import load_dotenv

load_dotenv()
login_senha = os.getenv("loginsenha")

url = "https://lit.stays.com.br"
endpoint = "/external/v1/booking/reservations-export"

querystring = {"from": "2023-12-10", "to": "2023-12-12", "dateType": "creation"}

headers = {"Authorization": f"Basic {login_senha}"}

response = requests.get(url, headers=headers, params=querystring)
print(response.status_code)
