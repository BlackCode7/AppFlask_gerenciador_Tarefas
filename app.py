from flask import Flask
import config
from flask_restx import Api
from controllers.LoginController import login_controller
from controllers.LoginController import api as ns_login
from controllers.LoginController import api as ns_usuario
from controllers.UsuarioController import usuario_controller
from flask_cors import CORS

# Instancia do Flask
app = Flask(__name__)

# Instancia do CORS
CORS(app)

# Instancia do flask_restx
api = Api(
    app,
    version='1.0',
    title='Gerenciador de Tarefas',
    description='Aplicação gerenciador de tarefas',
    doc='/docs'
)


def register_blueprints():
    app.register_blueprint(login_controller, url_prefix=config.API_BASE_URL)
    app.register_blueprint(usuario_controller, url_prefix=config.API_BASE_URL + '/usuario')


def add_namespaces():
    api.add_namespace(ns_login, path=config.API_BASE_URL)
    api.add_namespace(ns_usuario, path=config.API_BASE_URL + '/usuario')


if __name__ == '__main__':
    # api.base_url(config.API_BASE_URL)#4
    register_blueprints()  # 3
    add_namespaces()  # 2
    print(config.SECRET_KEY)
    app.run(host=config.API_HOST, port=config.API_PORT, debug=config.DEBUG)