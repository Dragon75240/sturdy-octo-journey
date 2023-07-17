import http.client
import os
from discord import Webhook

webhookURL = os.getenv('WEBHOOK_URL')

connection = http.client.HTTPConnection(webhookURL)

webhook = Webhook.from_url(webhookURL, session=connection)
webhook.send("sad", username="sdasd")

connection.close()