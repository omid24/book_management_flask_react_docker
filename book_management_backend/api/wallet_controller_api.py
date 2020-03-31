import json

from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from common.sanitize_param import sanitize_param
from models.user_model import User
from models.wallet_model import Wallet


class WalletController(Resource):

    # @jwt_required
    # def get(self):
    #
    #     current_user = get_jwt_identity()
    #     if current_user:
    #         result = User.find_one_username(current_user)
    #         _id = result.get("_id")
    #         if _id:
    #             result = Wallet.find_one_wallet(_id)
    #             result_json = dict(
    #                 name=result.get("name"),
    #                 budget_amount=result.get("budget_amount"),
    #                 account_number=result.get("account_number"),
    #                 user_id=str(result.get("user_id"))
    #
    #             )
    #             return result_json, 200
    #     return {"message": "yessss"}, 400

    # @jwt_required
    # def post(self):
    #
    #     data = json.loads(request.get_data())
    #     if not data:
    #         return {"message": "data not found in body request"}, 404
    #
    #     fields = ["name", "budget_amount", "account_number", "user_id"]
    #     for field in fields:
    #         if not data.get(field):
    #             return {"message": "field not found in json body"}, 404
    #
    #     name = sanitize_param(data.get("name"))
    #     budget_amount = sanitize_param(data.get("budget_amount"))
    #     account_number = sanitize_param(data.get("account_number"))
    #     user_id = sanitize_param(data.get("user_id"))
    #
    #     if Wallet.exist_wallet_user(user_id):
    #         return {"message": "Wallet exists"}, 404
    #
    #     is_inserted = Wallet.insert_wallet(name, budget_amount, account_number, user_id)
    #     if is_inserted:
    #         return {"message": "Wallet created"}, 200
    #     else:
    #         return {"message": "Wallet does not created"}, 404

    def get(self):

        result = Wallet.find_all()
        result_json = result
        return result_json, 200

    def post(self):

        data = json.loads(request.get_data())
        if not data:
            return {"message": "data not found in body request"}, 404

        print(data)

        fields = ["name", "budget_amount", "account_number"]
        for field in fields:
            if not data.get(field):
                return {"message": "field not found in json body"}, 404

        name = sanitize_param(data.get("name"))
        budget_amount = sanitize_param(data.get("budget_amount"))
        account_number = sanitize_param(data.get("account_number"))

        is_inserted = Wallet.insert_wallet_without_user(name, budget_amount, account_number)
        if is_inserted:
            return {"message": "Wallet created"}, 200
        else:
            return {"message": "Wallet does not created"}, 404

    def delete(self):
        data = json.loads(request.get_data())
        if not data:
            return {"message": "data not found in body request"}, 404

        print(data)

        fields = ["_id"]
        for field in fields:
            if not data.get(field):
                return {"message": "field not found in json body"}, 404

        _id = sanitize_param(data.get("_id"))
        result = Wallet.delete_id(_id)
        print(result)
        return {"message": "Wallet deleted with _id: %s" % _id}, 200
