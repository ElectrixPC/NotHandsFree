import os
import redis
from flask import Flask
from flask_sockets import Sockets
from raven.contrib.flask import Sentry

app = Flask(__name__)
app.config['REDIS_URL'] = os.environ['REDISTOGO_URL']
app.config['REDIS_CHAN'] = "nothandsfree"

sentry = Sentry(app)
redis = redis.from_url(app.config['REDIS_URL'])
sockets = Sockets(app)

from NotHandsFree.ws import Backend
backend = Backend()
backend.start()

from NotHandsFree import views