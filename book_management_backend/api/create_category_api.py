import json
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required


class CreateCategory(Resource):

    @jwt_required
    def post(self):
        data = json.loads(request.get_data())
        if not data:
            return {"error": "data not found in body request"}, 404

        return {"message": "asdasdasd"}, 200
