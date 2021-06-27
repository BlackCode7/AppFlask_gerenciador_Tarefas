import json
from flask import Blueprint, request, Response
from flask_restx import Resource
import config
from dtos.ErroDTO import ErroDTO
from dtos.UsuarioDTO import UsuarioLoginDTO
from services import JWTService
from swagger.LoginModel import user_fields, login_fields, api


login_controller = Blueprint('login_controller', __name__)


@login_controller.route('/login', methods=['POST'])
class Login(Resource):
    # respostas da api
    @api.doc(responses={200: "Login realizado com sucesso!"})
    @api.doc(responses={400: "Parâmetro de entrada inválido!"})
    @api.doc(response={500: "Não possível efetuar o login, tente novamente!"})
    @api.response(200, 'Sucesso', user_fields)
    # campos esperados e necessários para api
    @api.expect(login_fields)
    def post(self):
        try:
            body = request.get_json()

            if not body or "login" not in body or "senha" not in body:
                return Response(
                    json.dumps(ErroDTO("Parâmetro de entrada inválido!", status=400).__dict__),
                    status=400, mimetype='application/json')

            if body["login"] == config.LOGIN_TESTE and body["senha"] == config.SENHA_TESTE:
                id_usuario = 1  # usuario mocado deve ser trocado
                token = JWTService.gerar_token(id_usuario)

                return Response(
                    json.dumps(UsuarioLoginDTO("Admin", config.LOGIN_TESTES, token).__dict__),
                    status=200,
                    mimetype='application/json'
                )

            return Response(
                json.dumps(ErroDTO("Usuario ou senha incorreto", 401).__dict__),
                status=401,
                mimetype='application/json'
            )

        except Exception as e:
            print(e)
            return Response(
                json.dumps(ErroDTO('Falha ao fazer o Login', status=400).__dict__),
                status=500, mimetype='application/json')
