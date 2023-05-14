from flask import Flask

app = Flask("Servak")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

@app.route('/')
def index():
    return "Hello world"

app.run(host='0.0.0.0', port=8081)