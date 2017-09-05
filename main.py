from flask import Flask, request,jsonify, json, Response

# import config
import data, os

app = Flask(__name__)

client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')

button_link ='<a href="https://slack.com/oauth/authorize?client_id=' + client_id + '&scope=commands,channels:write">'
button_image = '<img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcset="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" /></a>'

@app.route("/install")
def add_to_slack():
    return Response(button_link + button_image)


@app.route("/")
def index():
    return 'Does this work?'

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


@app.route("/oauth")
def auth_route():
	url = 'https://slack.com/api/oauth.access'
	code = request.args.get("code")
	pay = {'code': code, 'client_id':CLIENT_ID, 'client_secret': CLIENT_SECRET}
	r = requests.get(url, pay)
	return 'that works'

@app.route("/test_endpoint", methods = ["POST"])
def test_endpoint():
    return "This is just to test everything is working"

@app.route("/attachment_route", methods = ["POST"])
def attach_text():
    return jsonify(data.attachment_text)

@app.route("/standard_message", methods = ['POST'])
def test_route():
	return jsonify(data.button_text)

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

@app.route("/phone_number_test", methods = ['POST'])
def pnt():
    return "<tel:+1234-5555">

if __name__ == '__main__':
    # app.run(port=4390)
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host='0.0.0.0',port=port)