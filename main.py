import os
from discord import Webhook


webhook = Webhook.from_url(os.environ("WEBHOOK_URL"))

webhook.send("sad", username="sdasd")

