import json

from bson import ObjectId
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from common.sanitize_param import sanitize_param
from models.buy_model import Buy
from models.wallet_model import Wallet


class BuyController(Resource):

    @jwt_required
    def post(self):

        data = json.loads(request.get_data())
        if not data:
            return {"message": "data not found in body request"}, 404


        fields = ["name", "price", "user_id"]
        for field in fields:
            if not data.get(field):
                return {"message": f"{field} not found in json body"}, 404

        name = sanitize_param(data.get("name"))
        price = sanitize_param(data.get("price"))
        user_id = ObjectId(sanitize_param(data.get("user_id")))

        if not Wallet.exist_wallet_user(user_id):
            return {"message": "Wallet exists"}, 404

        wallet = Wallet.find_one_wallet(user_id)
        if wallet:
            budget_amount = wallet.get("budget_amount", 0)
            if budget_amount:
                final_budget_amount = budget_amount - price
                if final_budget_amount < 0:
                    return {"message": "budget amount is not enough"}, 404
                else:
                    inserted_id = Buy.insert_buy(name, price, user_id)
                    if inserted_id:
                        update_wallet = Wallet.update_budget_amount(user_id, final_budget_amount)
                        if update_wallet:
                            return {"message": "Wallet updated"}, 200
                        else:
                            Buy.delete_buy(inserted_id)
                            return {"message": "wallet does not insert"}, 400
                    else:
                        Buy.delete_buy(inserted_id)

                return {"message": "Wallet created"}, 200
            return {"message": "Wallet budget_amount"}, 400
        else:
            return {"message": "Wallet does not created"}, 404
