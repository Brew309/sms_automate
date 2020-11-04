import random
from twilio.rest import Client
from texts_helpers import twilio_number, cellphone, account_sid, auth_token

# Create list containing texts
TEXTS = ['Hey, babe!',
'I dont cook, I dont clean but let me tell you how I got this ring.']

# Choose a text from list at random
quote = TEXTS[random.randint(0, (len(TEXTS) - 1))]

# Contact api and send text at specified time everyday
client = Client(account_sid, auth_token)

client.messages.create(
    body = quote,
    from_ = twilio_number,
    to = cellphone
    )



