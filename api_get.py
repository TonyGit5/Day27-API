
import json
import requests
from datetime import datetime

start_date = "2024-10-18"
API_KEY = "97597560372349699384541deea30fd8"
url = "https://newsapi.org/v2/everything?" \
    f"q=tesla&from={start_date}&sortBy=publishedAt&apiKey={API_KEY}"

#print (url)

request = requests.get(url)
content = request.text

print (content)