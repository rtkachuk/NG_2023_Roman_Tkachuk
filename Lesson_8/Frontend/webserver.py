from flask import Flask, render_template

app = Flask("Frontend")

@app.route("/websockets")
def websockets():
    return render_template("websockets.html")

@app.route("/ajax")
def ajax():
    return render_template("ajax.html")

app.run(host="0.0.0.0", port=8081)