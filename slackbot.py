import newrelic.agent
newrelic.agent.initialize()

from app import app
import api
