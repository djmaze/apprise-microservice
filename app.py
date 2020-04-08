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

@app.route('/', methods=['POST'])
def hello_world():
    data = request.get_json(force=True)
    apobj.notify(
        title=data['title'],
        body=data['body'],
    )
    return 'ok'
