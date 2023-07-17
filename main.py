import os
from discord import Webhook

webhookURL = os.getenv('WEBHOOK_URL')

print(webhookURL)

webhook = Webhook.from_url(webhookURL)

webhook.send("sad", username="sdasd")