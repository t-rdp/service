from flask import Flask, Blueprint
from flask_cors import CORS
import logging
import misc

app = Flask(__name__,
    static_folder = '../static',
    static_url_path = '/platform/static',
    template_folder = '../templates',
)
route = Blueprint(__name__ + "_bp", __name__ + "_bp")

CORS(app, origins = "*", supports_credentials = True)

# Load All Submodules
import service.newbie
import service.home

# Load BP
app.register_blueprint(route, url_prefix="/platform")