from flask import Blueprint


login_controller = Blueprint('login_controller', __name__)


@login_controller.route('/login', methods=['POST'])
def login():
    pass