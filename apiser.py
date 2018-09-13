from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
import json
import idiotDB

app = Flask(__name__)

idiotDB.defaultdb("database")


@app.route("/etkinlikler")
def etkinlikler():
    resp = Response(response=idiotDB.all("etkinlikler"),
    status=200,
    mimetype="application/json")
    return resp

@app.route("/yonetim")
def yonetim():
    return Response(response=idiotDB.all("yonetim"),
    status=200,
    mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=True)
