from flask import Blueprint, render_template

module = Blueprint('module', __name__)


@module.route('/index/', methods=['GET'])
def index():
    return render_template("module/index.html")
