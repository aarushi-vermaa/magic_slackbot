# my slackbot

import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
from flask import jsonify

# loads environment variables from the .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

print(f"Slack Token is {os.environ['SLACK_TOKEN']}")
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World!'

@app.route('/slack/<msg>')
def send(msg):
    print(f"Send message {msg}")
    return jsonify(msg)

@app.route('/slack2/<msg>')
def send2(msg):
    print(f"Send message {msg}")
    client.chat_postMessage(channel='#general', text=f'{msg}')
    return jsonify(msg)
    

client.chat_postMessage(channel='#general', text='Hola! Yes, I am alive here too')


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
    # will this thing run in default port, 5000?
    # "debug" : if I save this file, modify it, I dont need to run the python script again. It will automatically update the web server