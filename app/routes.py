from app import app

from flask import Flask, request, jsonify, json, Response, render_template
import requests
import os
client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')

# Just a base homepage to show it working without using Slack
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


# This is for allowing the installation of the app to a team
@app.route("/install")
def add_to_slack():
    return render_template('install.html', client_id=client_id)

######################
# Errors start here: #
######################


# Error handling for 404
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist - 404', 404

# Error handling 503
@app.errorhandler(503)
def error_503_page(error):
    return 'This is the 503 page', 503
