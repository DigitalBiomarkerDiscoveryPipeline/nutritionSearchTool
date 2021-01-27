# Author:       Lucy (theBlackFemaleEngineer)
# Date:         28 October 2020
# Description:  This is a basic main file for the nutrition API server

from flask import Flask, request, Response
from actualAPI import *

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    """ Return a friendly HTTP greeting. """
    resp = Response("evoo!")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/get_random_nutrients/", methods=["GET"])
def nutrients():
    """ Return a friendly HTTP greeting. """
    search = request.args.get("search", "apple")
    output = test(search)
    resp = Response(output)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)
