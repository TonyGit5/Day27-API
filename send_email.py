import smtplib, ssl
import os

block = False

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    receiver = "tdimambro@comcast.net"

    with open ("cred.txt") as cred:
        creds = cred.readlines()
        user = creds[0].strip("\n")
        password = creds[1]
        #password = os.getenv("PASSWD")
    #print (creds)
    #print (user, password)

    if not block:
        context = ssl.create_default_context()
        #...context=context => name_of_variable = variable keyword=variable in the .SMTP_SSL Method
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(user, password)
            server.sendmail(user, receiver, message)
