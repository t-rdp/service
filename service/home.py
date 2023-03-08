from service import route
from flask import render_template
from service.middleware import authRequired

@route.route("/home")
@authRequired()
def home(*, id, ud, i):
    return render_template("home.html")