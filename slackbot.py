import newrelic.agent
newrelic.agent.initialize('config/newrelic.ini')

from app import app
# imports the api routes
import api
