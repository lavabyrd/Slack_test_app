from app import app
from flask import render_template

# Just a base homepage to show it working without using Slack
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')