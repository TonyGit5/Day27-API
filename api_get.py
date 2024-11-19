
import json
import requests
from datetime import datetime
import send_email as mail
import unicodedata
from unidecode import unidecode

start_date = "2024-10-19"
topic = "tesla"
block = False
mail_content = []


def api_call(start_date, topic):
    
    API_KEY = "97597560372349699384541deea30fd8"
    url = "https://newsapi.org/v2/everything?" \
        f"q={topic}&from={start_date}&language=en&sortBy=publishedAt" \
            f"&apiKey={API_KEY}"

    #print (url)

    request = requests.get(url)
    content = request.json()

    return (content)

def parser(content):
    pass

if __name__ == "__main__":

    content = api_call(start_date, topic)
    print (content)
    print (content['status'])
    print (content['totalResults'])
  
    # Gather Article Source, Title, Description and url

    for article in content['articles']:
        #print (f"{article['source']['name']} -- {article['title']} \n {article['description']} \n {article['url']} \n")
        mail_content.append(str(f"{article['title']}  --  {article['source']['name']}\n {article['description']} \n {article['url']} \n"))
    #print (mail_content)
    #mail_content = mail_content.encode("utf-8")
    mail_data = ""
    #mail_content = parser(content)
    for item in mail_content:
        mail_data = mail_data + unidecode(item)
                    
    mail.send_mail(mail_data)
    
    
    #
    #
    #print (content['articles'])