import http.client
import os
from time import sleep
import discordwebhook as dwh

webhookURL = os.getenv('WEBHOOK_URL')

webhook = dwh.Discord(url=webhookURL)

for i in range(50):
    webhook.post(content="@dragonning ")