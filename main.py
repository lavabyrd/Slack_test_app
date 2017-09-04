from flask import Flask, request,jsonify, json, Response

import config, data

app = Flask(__name__)

client_id = config.CLIENT_ID
client_secret = config.CLIENT_SECRET

@app.errorhandler(500)
def page_not_found(error):
    return 'This page does not exist', 500


@app.route("/oauth")
def auth_route():
	url = 'https://slack.com/api/oauth.access'
	code = request.args.get("code")
	pay = {'code': code, 'client_id':CLIENT_ID, 'client_secret': CLIENT_SECRET}
	r = requests.get(url, pay)
	return 'that works'

@app.route("/test_endpoint", methods = ["POST"])
def test_endpoint():
    return 'this is a test endpoint'

@app.route("/standard_message", methods = ['POST'])
def test_route():
	return jsonify(data.example_text)

@app.route("/output", methods = ['POST'])
def output_route():

	    # Parse the request payload
    form_json = json.loads(request.form["payload"])
    

    # Check to see what the user's selection was and update the message
    selection = form_json["actions"][0]["value"]
    

    if selection == "war":
        message_text = "The only winning move is not to play.\nHow about a nice game of chess?"
    else:
        message_text = ":horse:"

    return Response(message_text)


if __name__ == '__main__':
    app.run(port=4390)