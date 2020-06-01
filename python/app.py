import os
import requests
import pprint

from flask import Flask,request
app = Flask(__name__)

# Listen on route '/sms-webhook' for GET/POST requests
@app.route('/sms-webhook', methods=['POST'])
def sms_webhook():
    # Forward incoming form data to email
    send_email(pprint.pformat(request.form, indent=4))
    return "200"

# Send email with MailGun
def send_email(body):
    return requests.post(
        "https://api.mailgun.net/v3/" + os.environ['MAILGUN_DOMAIN'] + "/messages",
        auth=("api", os.environ['MAILGUN_API_TOKEN']),
        data={"from": os.environ['EMAIL_FROM'],
              "to": [os.environ['EMAIL_TO']],
              "subject": os.environ['EMAIL_SUBJECT'],
              "text": body })

# Listen on '/' for default requests
@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
