
import json
import requests
from datetime import datetime
import send_email as mail

start_date = "2024-10-18"
topic = "tesla"
block = False

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
    print (content['status'])
    print (content['totalResults'])
  
    for article in content['articles']:
        #print (f"{article['source']['name']} -- {article['title']} \n {article['description']} \n {article['url']} \n")
        mail_content = (f"{article['source']['name']} -- {article['title']} \n {article['description']} \n {article['url']} \n")
    
    #mail_content = parser(content)
    #mail.send_mail(mail_content)
    
    
    #
    #
    #print (content['articles'])