import requests

url = "https://slack.com/api/chat.postMessage"
OAuth_Token="xoxp-375212089761-375532316308-1027901139504-bb9ff8728a671490c9ead3bf0c58db56"
Bot_Token="xoxb-375212089761-1026979595861-Nal2WIeTjC8aHCvZAPobVbK5"
CHANNEL_ID="DB1682UGH"

data = {
   "token": OAuth_Token,
   "channel": CHANNEL_ID,
   "text": "Hello world"
}

requests.post(url, data=data)
