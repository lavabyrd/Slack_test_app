from flask import request, jsonify, json, Response, Flask
from app import app
import os
import requests


client_id = app.config['CLIENT_ID']
client_secret = app.config['CLIENT_SECRET']
oauth_token = app.config['OAUTH_TOKEN']

# Oauth verification endpoint, required to get the requester code and verify


@app.route("/oauth")
def auth_route():
    url = 'https://slack.com/api/oauth.access'
    code = request.args.get("code")
    pay = {'code': code, 'client_id': client_id,
           'client_secret': client_secret}
    r = requests.get(url, pay)
    print(r.text)
    return 'that works' + str


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
@app.route("/EVENT", methods=["POST"])
def got_event():
    out2 = request.args.get("token")
    out1 = request.get_json()
    print(out1)
    # print(out1['event']['text'])

    try:
        return out1['challenge']

    except:
        return "ran"
    # challenge = out1['challenge']
    # print(request.get_json())

    # return "done"
    # out = request.get_json()
    # print(out)
    # return "good to go!"


# Endpoint that returns a basic formatted message from data.py
@app.route("/attachment_route", methods=["POST"])
def attach_text():
    return jsonify(attachment_text)


# Endpoint that returns some interactive buttons
@app.route("/interactive_buttons", methods=['POST'])
def interaction_button_route():
    return jsonify(button_text)

# Endpoint used to create a message that has a "Show More" message attachment


@app.route("/space_check", methods=['POST'])
def space_check():
    return jsonify(show_more_attachment)


# Output for the interactive buttons
@app.route("/output", methods=['POST'])
def output_route():
    form_json = json.loads(request.form["payload"])
    selection = form_json["actions"][0]["value"]
    return selection_output(selection)


# Function to control logic of the buttons
def selection_output(selection):
    if selection == "war":
        message_text = "The only winning move is not to play.\n How about a nice game of chess?"
    else:
        message_text = ":horse:"

    return Response(message_text)


@app.route("/dialog", methods=['POST'])
def dialog_endpoint():
    return "hi"


button_text = {
    "text": "Would you like a game?",
    "attachments": [
        {
            "text": "What would you like to do?",
            "fallback": "You are unable to choose a game",
            "callback_id": "wopr_game",
            "color": "#3AA3E3",
            "attachment_type": "default",
            "actions": [
                {
                    "name": "game",
                    "text": "Chess",
                    "type": "button",
                    "value": "chess"
                },
                {
                    "name": "game",
                    "text": "Falken's Maze",
                    "type": "button",
                    "value": "maze"
                },
                {
                    "name": "game",
                    "text": ":thumbsup:",
                    "type": "button",
                    "value": "blah"
                },
                {
                    "name": "game",
                    "text": "Thermonuclear War",
                    "style": "danger",
                    "type": "button",
                    "value": "war",
                    "confirm": {
                        "title": "Are you sure?",
                        "text": "Wouldn't you prefer a good game of chess?",
                        "ok_text": "Yes",
                        "dismiss_text": "No"
                    }
                }
            ]
        }
    ]
}

attachment_text = {
    "attachments": [{
        "text": ":thumbsup: F0 9F 8C 8A",
        "color": "#36a64f",
        "mrkdwn": True
    }]
}

attachment_text2 = {
    "attachments": [{
        "text": "Optional text that \n \n \n \n   appears within the attachment",
        "color": "#36a64f",
        "mrkdwn": True
    }]
}

show_more_attachment = {
    "attachments": [
        {
            "fallback": "Required plain-text summary of the attachment.",
            "color": "#36a64f",
            "pretext": "Optional text that appears above the attachment block",
            "author_name": "Bobby Tables",
            "author_link": "http://flickr.com/bobby/",
            "author_icon": "http://flickr.com/icons/bobby.jpg",
            "title": "Slack API Documentation",
            "title_link": "https://api.slack.com/",
            # This should not require spaces after each \n but change happened about March 18th
            "text": "Optional text that \n \n \n \n \n \n \n appears within the attachment",
            "fields": [
                {
                    "title": "Priority",
                    "value": "High",
                    "short": "false"
                }
            ],
            "image_url": "http://my-website.com/path/to/image.jpg",
            "thumb_url": "http://example.com/path/to/thumb.png",
            "footer": "Slack API",
            "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
            "ts": 123456789
        }
    ]
}
