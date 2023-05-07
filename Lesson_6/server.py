from flask import Flask, render_template, redirect, request
from dbWorker import *

DB_PATH = "users.db"

servak = Flask("Users example")
init_tables(DB_PATH)

@servak.route('/')
def index():
    usersTable = generateLoginsHTMLTalbe(getLogins(DB_PATH))
    return render_template("index.html", users=usersTable)

@servak.route('/register', methods=['POST'])
def register():
    login = str(request.form.get('login'))
    passw = str(request.form.get('password'))
    registerUser(DB_PATH, login, passw)
    return redirect('/', code=302)

servak.run(host='0.0.0.0', port=8081)