import base64
import smtplib
import secrets
import threading

from gevent.pywsgi import WSGIServer
from gevent import monkey
monkey.patch_all()

import misc
import service
from service import app

app.debug = misc.config["service"]["debug"] == 1

if not app.debug:
    http_server = WSGIServer(('0.0.0.0', int(misc.config["service"]["port"])), app)
    http_server.serve_forever()
else:
    app.run("0.0.0.0", misc.config["service"]["port"], debug=app.debug)