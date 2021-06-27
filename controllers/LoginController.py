import json
from flask import Blueprint, request, Response
from flask_restx import Namespace, Resource, fields

from dtos.ErroDTO import ErroDTO
from swagger.LoginModel import user_fields, login_fields

login_controller = Blueprint('login_controller', __name__)
api = Namespace('login', description='Realiza login na aplicação')


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

            if "login" not in body or "senha" not in body:
                return Response(
                    json.dumps(ErroDTO("Parâmetro de entrada inválido!", status=400).__dict__),
                    status=400, mimetype='application/json')

            return Response("Login efetuado com sucesso!",
                status=200, mimetype='application/json')

        except Exception as e:
            print(e)
            return Response(
                json.dumps(ErroDTO('Falha ao fazer o Login', status=400).__dict__),
                status=500, mimetype='application/json')


"""

        if not body or "login" not in body or "senha" not in body:
            return Response("Parametros Inválidos",
                            status=400, mimetype='application/json')

"""