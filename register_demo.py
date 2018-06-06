from flask import Blueprint

register = Blueprint('register',__name__)


@register.route('/register')
def reg():
    return 'register'