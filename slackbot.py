import newrelic.agent
newrelic.agent.initialize('config/newrelic.ini')

from app import app
import api
