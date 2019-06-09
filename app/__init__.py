from flask import Flask

app = Flask(__name__)

app.config.from_object('config')

# import and register our module controllers (or views)
from app.module.controllers import module
app.register_blueprint(module)
