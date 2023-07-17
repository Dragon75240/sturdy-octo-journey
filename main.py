import os
import aiohttp
from discord import Webhook

webhookURL = os.getenv('WEBHOOK_URL')

async def main():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(webhookURL, session=session)

        webhook.send("sad", username="sdasd")

main()