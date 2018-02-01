from flask import request, jsonify, json, Response
# import the main app instance
from app import app

@app.route('/api')
def api_index():
    return "hmm"
