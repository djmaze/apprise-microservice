import apprise
import os
from flask import Flask, request

urls = os.environ['NOTIFICATION_URLS']

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
