import os
import discordwebhook as dwh

webhookURL = os.getenv('WEBHOOK_URL')

webhook = dwh.Discord(url=webhookURL)

while True:
    webhook.post(content="@everyone ")