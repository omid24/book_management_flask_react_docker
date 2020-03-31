import json
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from models.user_model import User
from flask_jwt_extended import jwt_required


class LoginUser(Resource):
    def post(self):
        data = json.loads(request.get_data())
        if not data:
            return {"error": "data not found in body request"}, 404

        username = data.get("username")
        if not username:
            return {"error": "username not found in json body"}, 404

        password = data.get("password")
        if not password:
            return {"error": "password not found in json body"}, 404

        is_auth = User.authentication_user(username, password)
        if is_auth:
            access_token = create_access_token(identity=username)
            return {"access_token": access_token}, 200

        return {"error": "username or password is not correct"}, 401
