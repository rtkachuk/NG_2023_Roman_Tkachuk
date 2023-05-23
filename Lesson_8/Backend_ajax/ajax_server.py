from flask import Flask, make_response
from datetime import datetime

app = Flask("Ajax_server")

@app.route("/gettime")
def getTime():
    response = make_response(str(datetime.now()))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

app.run(host="0.0.0.0", port=8083)