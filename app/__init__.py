from flask import Flask
import os
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

from app import routes


# App startup
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    app.run(debug=True,host='0.0.0.0', port=port)
