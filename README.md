# Forward Messages to Email 
This super simple guide will show how you can handle incoming messages and forward them to an email address. We will use the [SignalWire Python SDK](https://developer.signalwire.com/twiml/reference/client-libraries-and-sdks#python) to handle the incoming message and [MailGun API](https://www.mailgun.com/) to send an email.

# Setup Your Environment File
Copy from example.env and fill in your values
Save new file called .env

Your file should look something like this.

```
## This is the full name of your SignalWire Space. e.g.: example.signalwire.com
SIGNALWIRE_SPACE=
# Your Project ID - you can find it on the `API` page in your Dashboard.
SIGNALWIRE_PROJECT=
# Your API token - you can generate one on the `API` page in your Dashboard
SIGNALWIRE_TOKEN=
# The phone number you'll be using for this guide. Must include the `+1` , 
SIGNALWIRE_NUMBER=
# MailGun domain associated with your MailGun account
MAILGUN_DOMAIN=
# MailGun token associated with your MailGun Account
MAILGUN_API_TOKEN=
# Send Email From Address
EMAIL_FROM=info@yourdomain.com
# Send email to address for administrator notifications
EMAIL_TO=youremail@yourdomain.com
# Email subject for admin notifications
EMAIL_SUBJECT=Forward Text To Email
```

# Step by Step Code Walkthrough
This code is actually very simple - you need only one route and one function! The first step is to define a function `send_email(body)` that will utilize the MailGun API to send an email using the variables from our `.env` file.

```python
# Send email with MailGun
def send_email(body):
    return requests.post(
        "https://api.mailgun.net/v3/" + os.environ['MAILGUN_DOMAIN'] + "/messages",
        auth=("api", os.environ['MAILGUN_API_TOKEN']),
        data={"from": os.environ['EMAIL_FROM'],
              "to": [os.environ['EMAIL_TO']],
              "subject": os.environ['EMAIL_SUBJECT'],
              "text": body })
```
Our only route `/sms-webhook` will listen for POST requests from incoming messages and will use the JSON form data as the body of the email. 

```python
# Listen on route '/sms-webhook' for GET/POST requests
@app.route('/sms-webhook', methods=['POST'])
def sms_webhook():
    # Forward incoming form data to email
    send_email(pprint.pformat(request.form, indent=4))
    return "200"
```

# Build and Run on Docker

Use our pre-built image from Docker Hub

```
docker pull signalwire/snippets-text-to-email:python
```

Or build your own image and run!

```
docker build -t snippets-text-to-email .
docker run --publish 5000:5000 --env-file .env snippets-text-to-email
```

The application will run on port 5000.

# Build and Run Natively

To run the application, execute export FLASK_APP=app.py then run flask run.

You may need to use an SSH tunnel for testing this code if running on your local machine. – we recommend [ngrok](https://ngrok.com/). You can learn more about how to use ngrok [here](https://developer.signalwire.com/apis/docs/how-to-test-webhooks-with-ngrok). 

# Sign Up Here

If you would like to test this example out, you can create a SignalWire account and space [here](https://m.signalwire.com/signups/new?s=1).

Please feel free to reach out to us on our Community Slack or create a Support ticket if you need guidance!
