from flask import request, jsonify, json, Response, Flask
# import the main app instance
from app import app
import os
import requests

client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')
oauth_token = os.environ.get('SLACK_BOT_TOKEN')

# Oauth verification endpoint, required to get the requester code and verify
@app.route("/oauth")
def auth_route():
    url = 'https://slack.com/api/oauth.access'
    code = request.args.get("code")
    pay = {'code': code, 'client_id': client_id,
           'client_secret': client_secret}
    r = requests.get(url, pay)
    return 'that works'


##################
# Slash commands #
##################


# returns a link to the heroku page for this app
@app.route("/app_link", methods=['POST'])
def app_link():
    return 'https://python-slack-app.herokuapp.com'


# Endpoint with basic response
@app.route("/basic_test_endpoint", methods=["POST"])
def basic_test_endpoint():
    print(request.__dict__)
    return "This should work"


# Endpoint for events and challenge. Uncomment for verification url
@app.route("/event", methods=["POST"])
def got_event():
    # output = request.args.get("token")
    # challenge = out['challenge']
    # print("form is " + challenge)
    # return challenge
    out = request.get_json()
    print(out)
    return "good to go!"


# Endpoint that returns a basic formatted message from data.py
@app.route("/attachment_route", methods=["POST"])
def attach_text():
    return jsonify(data.attachment_text)


# Endpoint that returns some interactive buttons
@app.route("/interactive_buttons", methods=['POST'])
def interaction_button_route():
    return jsonify(data.button_text)


# Output for the interactive buttons
@app.route("/output", methods=['POST'])
def output_route():
    form_json = json.loads(request.form["payload"])
    selection = form_json["actions"][0]["value"]
    return selection_output(selection)


# Function to control logic of the buttons
def selection_output(selection):
    if selection == "war":
        message_text = "The only winning move is not to play.\nHow about a nice game of chess?"
    else:
        message_text = ":horse:"

    return Response(message_text)
