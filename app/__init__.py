from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application and database object
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# import and register our module controllers (or views)
from app.module.controllers import module

app.register_blueprint(module)

db.create_all()
