import apprise
import os
from flask import Flask, request

if 'NOTIFICATION_URLS' in os.environ.keys():
    urls = os.environ['NOTIFICATION_URLS']
elif 'NOTIFICATION_URLS_FILE' in os.environ.keys():
    with open(os.environ['NOTIFICATION_URLS_FILE'], 'r') as secrets_file:
        urls = secrets_file.read()

apobj = apprise.Apprise()
apobj.add(urls)

app = Flask(__name__)

lastMessages = dict()

@app.route('/', methods=['POST'])
def hello_world():
    data = request.get_json(force=True)
    send = True
    if 'id' in data:
        state = data['state'] if 'state' in data else {'title': data['title'], 'body': data['body']}
        send = ('forceSend' in data and data['forceSend'] == 'true') or (not (data['id'] in lastMessages and lastMessages[data['id']] == state))
        lastMessages[data['id']] = state

    if send:
        apobj.notify(
            title=data['title'],
            body=data['body'],
            notify_type=data.get('notify_type', None),
        )
    return 'ok' if send else 'deduplicated'
