from flask_restx import fields, Namespace

from controllers.LoginController import api


api = Namespace('Login', description='Realizar login na aplicação!')

login_fields = api.model(
    'LoginDTO', {
        'login': fields.String,
        'senha': fields.String
    })

user_fields = api.model(
    'UsuarioDTO', {
        'name': fields.String,
        'email': fields.String,
        'token': fields.String,
    }
)