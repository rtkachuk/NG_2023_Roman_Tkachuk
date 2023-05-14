from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from servak import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)

class News(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text)
    desc = db.Column(db.Text)
    author = db.Column(db.Integer)
    creationDate = db.Column(db.DateTime)

