from flask import Flask
import os
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

from app import routes


