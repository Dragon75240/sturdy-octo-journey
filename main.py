import http.client
import os
from time import sleep
import discordwebhook as dwh

webhookURL = os.getenv('WEBHOOK_URL')

webhook = dwh.Discord(url=webhookURL)

for i in range(2):
    beep = False
    if (beep == False):
        sleep(210)
    webhook.post(content="@everyone")

# echgodag