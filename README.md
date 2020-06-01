# Snippets Text To Email
This snippets will show you how to forward text messages to a email account.
## About Text To Email
Have you wanted a way to allow your customers to send you a quick message or wanted to take a quick note. This text to email example will allow you to do just that.
## Getting Started
You will need a machine with Python installed, the SignalWire SDK, a provisioned SignalWire phone number, and optionaly Docker if you decide to run it in a container.

For this demo we will be using Python, but more languages may become available.

- [x] Python
- [x] SignalWire SDK
- [x] SignalWire Phone Number
- [x] MailGun Account (For administrator notifications, https://www.mailgun.com/)
- [x] Docker (Optional)
----
## Running Text To Email - How It Works
## Methods and Endpoints

```
Endpoint: /sms-webhook
Methods: GET OR POST
Endpoint to accept incoming text messages from SignalWire space and forward them to MailGun.
```

## Setup Your Enviroment File

1. Copy from example.env and fill in your values
2. Save new file callled .env

Your file should look something like this
```
## This is the full name of your SignalWire Space. e.g.: example.signalwire.com
SIGNALWIRE_SPACE=
# Your Project ID - you can find it on the `API` page in your Dashboard.
SIGNALWIRE_PROJECT=
# Your API token - you can generate one on the `API` page in your Dashboard
SIGNALWIRE_TOKEN=
# The phone number you'll be using for this Snippets. Must include the `+1` , e$
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

## Build and Run on Docker
Lets get started!
1. Use our pre-built image from Docker Hub 
```
For Python:
docker pull signalwire/snippets-text-to-email:python
```
(or build your own image)

1. Build your image
```
docker build -t snippets-text-to-email .
```
2. Run your image
```
docker run --publish 5000:5000 --env-file .env snippets-text-to-email
```
3. The application will run on port 5000

## Build and Run Natively
For Python
```
1. Replace enviroment variables
2. From command line run, python3 app.py
```

----
# More Documentation
You can find more documentation on LaML, Relay, and all Signalwire APIs at:
- [SignalWire Python SDK](https://github.com/signalwire/signalwire-python)
- [SignalWire API Docs](https://docs.signalwire.com)
- [SignalWire Github](https://gituhb.com/signalwire)
- [Docker - Getting Started](https://docs.docker.com/get-started/)
- [Python - Gettings Started](https://docs.python.org/3/using/index.html)
- [MailGun](https://www.mailgun.com/)

# Support
If you have any issues or want to engage further about this Signal, please [open an issue on this repo](../../issues) or join our fantastic [Slack community](https://signalwire.community) and chat with others in the SignalWire community!

If you need assistance or support with your SignalWire services please file a support ticket from your Dashboard. 
