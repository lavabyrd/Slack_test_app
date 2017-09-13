from flask import Flask, request, jsonify, json, Response, render_template


import data, os, requests
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')


# This is for allowing the installation of the app to a team
@app.route("/install")
def add_to_slack():
    return render_template('install.html', client_id=client_id)


# Just a base homepage to show it working without using Slack
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/app_link", methods=['POST'])
def app_link():
    return 'https://python-slack-app.herokuapp.com'


# Error handling for 404 and 503
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


@app.errorhandler(503)
def error_503_page(error):
    return 'This is the 503 page', 503


# Oauth verification endpoint, required to get the requester code and verify
@app.route("/oauth")
def auth_route():
    url = 'https://slack.com/api/oauth.access'
    code = request.args.get("code")
    pay = {'code': code, 'client_id': client_id, 'client_secret': client_secret}
    r = requests.get(url, pay)
    return 'that works'


# Endpoint with basic response
@app.route("/test_endpoint", methods=["POST"])
def test_endpoint():
    # user = request.args.get("user")
    print(request.args)
    return "This should work"


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
