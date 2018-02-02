import newrelic.agent
newrelic.agent.initialize()

from app import app
import api
import os
# App startup
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    app.run(debug=True, host='0.0.0.0', port=port)
