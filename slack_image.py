import requests
import sys

url = "https://slack.com/api/files.upload"
imaege_file=sys.argv[1]


OAuth_Token="xoxp-375212089761-375532316308-1027901139504-bb9ff8728a671490c9ead3bf0c58db56"
Bot_Token="xoxb-375212089761-1026979595861-Nal2WIeTjC8aHCvZAPobVbK5"
CHANNEL_ID="DB1682UGH"

data = {
   "token": OAuth_Token,
   "channels": CHANNEL_ID,
   "title": "image file",
   #"initial_comment": "initial\ncomment"
   "initial_comment": "image dayo"
}

files = {'file': open(imaege_file, 'rb')}
requests.post(url, data=data, files=files)


