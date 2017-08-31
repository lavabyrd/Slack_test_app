from flask import Flask, request
import requests
app = Flask(__name__)


# just to add basic testing variables



@app.route("/")
def hello():
    return "Hello World!"

@app.errorhandler(500)
def page_not_found(error):
    return 'This page does not exist', 404


@app.route("/oauth")
def auth_route():
	url = 'https://slack.com/api/oauth.access'
	code = request.args.get("code")
	pay = {'code': code, 'client_id':CLIENT_ID, 'client_secret': CLIENT_SECRET}
	r = requests.get(url, pay)
	return 'that works'

@app.route("/test", methods = ['POST'])
def test_route():
	return 'Does this work, or not...'

if __name__ == '__main__':
    app.run(port=4390)