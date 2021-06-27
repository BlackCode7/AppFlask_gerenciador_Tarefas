from flask_restful import Resource


@usuario_controller.route('/login', methods=['POST'])
class Login(Resource):
    def post(self):
        pass