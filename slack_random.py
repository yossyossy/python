import requests

url = "https://slack.com/api/chat.postMessage"
OAuth_Token="xoxp-375212089761-375532316308-1027901139504-bb9ff8728a671490c9ead3bf0c58db56"
Bot_Token="xoxb-375212089761-1026979595861-Nal2WIeTjC8aHCvZAPobVbK5"
CHANNEL_R_ID="CB11SADL0"
CHANNEL_G_ID="CB1682V4Z"

data = {
   "token": OAuth_Token,
   "channel": CHANNEL_R_ID,
   "text": "Hello world"
}

requests.post(url, data=data)
