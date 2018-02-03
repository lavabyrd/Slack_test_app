from flask import Flask
import os
from flask_bootstrap import Bootstrap
try:
    from config import Config
except ImportError:
    raise ImportError('<no config files found>')

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(Config)

from app import routes


