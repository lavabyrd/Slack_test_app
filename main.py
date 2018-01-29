from flask import Flask, request, jsonify, json, Response, render_template
from flask_bootstrap import Bootstrap
import data
import os
import requests
from slackclient import SlackClient

app = Flask(__name__)
Bootstrap(app)

# client_id = os.environ.get('client_id')
# client_secret = os.environ.get('client_secret')
# bot_token = os.environ.get('bot_token')

client_id = "225895574304.243862096499"
client_secret = "aaacecc50dca74f35b92f5a48dcdae9d"
bot_token = "QBwvJxdOTIiFG2EiqQ0ExUVn"

SLACK_BOT_TOKEN = "xoxp-225895574304-225895574656-230549264020-9d3e9172248efe9fc43b2e3d8f483405"
slack_client = SlackClient(SLACK_BOT_TOKEN)
# This is for allowing the installation of the app to a team
@app.route("/install")
def add_to_slack():
    return render_template('install.html', client_id=client_id)


# Just a base homepage to show it working without using Slack
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/what")
def what_route():
    y = oauth_process()
    return y


@app.route("/app_link", methods=['POST'])
def app_link():
    return 'https://python-slack-app.herokuapp.com'


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


@app.errorhandler(503)
def error_503_page(error):
    return 'This is the 503 page', 503


# Oauth verification endpoint, required to get the requester code and verify
@app.route("/oauth")
def auth_route():
    x = oauth_process()
# Error handling for 404 and 503
    return x


def oauth_process():
    url = 'https://slack.com/api/oauth.access'
    code = request.args.get("code")
    pay = {'code': code, 'client_id': client_id, 'client_secret': client_secret}
    r = requests.post(url, pay)

    return "good to go"

# Endpoint with basic response
@app.route("/test_endpoint", methods=["POST"])
def test_endpoint():
    # print(request.get_json())
    print(request.__dict__)
    # print(request.form)
    return "This should work"

@app.route("/dialog", methods=["POST"])
def dialogOpen():
    # trigger = request.form["trigger_id"]
    message_action = request.form["token"]
    print(message_action)
    open_dialog = slack_client.api_call("dialog.open",
    trigger_id=message_action["trigger_id"],
    
    dialog={
                "title": "Request a coffee",
                "submit_label": "Submit",
                "callback_id":"coffee_order_form",
                "elements": [
                    {
                        "label": "Coffee Type",
                        "type": "select",
                        "name": "meal_preferences",
                        "placeholder": "Select a drink",
                        "options": [
                            {
                                "label": "Cappuccino",
                                "value": "cappuccino"
                            },
                            {
                                "label": "Latte",
                                "value": "latte"
                            },
                            {
                                "label": "Pour Over",
                                "value": "pour_over"
                            },
                            {
                                "label": "Cold Brew",
                                "value": "cold_brew"
                            }]}]})
    print (open_dialog)
    return "eh"



@app.route("/dialog_endpoint", methods=["POST"])
def dialog_endpoint2():
    return "hi"


# Endpoint for easier ngrok testing
@app.route("/test_endpoint2", methods=["POST"])
def test_endpoint2():
    user = request.form["user_id"]
    attachment_text = {
        "attachments": [{
            "text": "hey <@" + user + ">",
            "channel": "C6PJSM3V5",
            "color": "#36a64f",
            "mrkdwn": True
        }]
    }

    return jsonify(attachment_text)


# Endpoint that returns a basic formatted message from data.py
@app.route("/attachment_route", methods=["POST"])
def attach_text():
    return jsonify(data.attachment_text)


# Endpoint that returns some interactive buttons
@app.route("/interactive_buttons", methods=['POST'])
def test_route():
    return jsonify(data.button_text)


# Output for the interactive buttons
@app.route("/output", methods=['POST'])
def output_route():
    form_json = json.loads(request.form["payload"])
    selection = form_json["actions"][0]["value"]
    return selection_output(selection)


@app.route("/standard_message", methods=['POST'])
def standard_message():
    url = 'https://slack.com/api/chat.postMessage'

    data1 = {
        "token": bot_token,
        "ok": True,
        "channel": "C6PJSM3V5",
        "text": "something <@Mpreston-owner>"
    }
    requests.post(url, data=data1)
    return True


# Function to control logic of the buttons
def selection_output(selection):
    if selection == "war":
        message_text = "The only winning move is not to play.\nHow about a nice game of chess?"
    else:
        message_text = ":horse:"

    return Response(message_text)


# App startup
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port)
