import os
import discordwebhook as dwh

webhookURL = os.getenv('WEBHOOK_URL')

webhook = dwh.Discord(url=webhookURL)

for i in range(5):
    webhook.post(content="@Everyone")