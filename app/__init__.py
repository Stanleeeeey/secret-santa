from flask import Flask
import flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SECRET_KEY"] = 'zgaslo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db       = SQLAlchemy(app)

from app import model, routes, db_ops



with app.app_context():
    db.create_all()
    try:
        g = model.Group(name = "zdisie", budget = 10)
        db.session.add(g)
        db.session.commit()
    except: pass
    app.run()

print(__name__)