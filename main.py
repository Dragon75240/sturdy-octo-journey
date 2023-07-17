import os
import aiohttp
from discord import Webhook

webhookURL = os.getenv('WEBHOOK_URL')

print(webhookURL)

async def foo():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(webhookURL)

        webhook.send("sad", username="sdasd")