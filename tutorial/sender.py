import smtplib, ssl
import json

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "testonly@gmail.com"  # Enter sender address
password = 'asdfasdfasdf' # pwd for testonly@gmail.com
receiver_email = "yourPersonalEmail@gmail.com"  # Enter receiver address, usually your personal address.
# password = input("Type your password and press enter: ")
message = """\
Subject: Export Control License

"""

f = open('quotes.json')
message += json.dumps(json.load(f))
# print(message)
# print(type(message))


context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)