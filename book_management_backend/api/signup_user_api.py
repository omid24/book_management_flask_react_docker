import json
from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash

from models.user_model import User


class SignUpUser(Resource):

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

        exists_user = User.exists_username(username)
        if (exists_user is not None and exists_user) or exists_user is None:
            return {"error": "Username exist in database"}, 404

        User.insert_user(username, generate_password_hash(password))
        # check_password_hash(user['password'], password)
        print("data: ", data)
        return {"message": f"user created with username: {username} and password: {password}"}, 201
