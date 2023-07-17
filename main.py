import http.client
import os
import discordwebhook as dwh

webhookURL = os.getenv('WEBHOOK_URL')

webhook = dwh.Discord(url=webhookURL)

for i in range(50):
    webhook.post(content="ping test ||<@1054120939589210264>||")

# echgodag