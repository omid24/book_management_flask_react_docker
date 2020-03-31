from bson import ObjectId
from pymongo import MongoClient

from config.config import Config


class Buy:
    collection = MongoClient(Config.mongodb_connection_string)[Config.mongodb_db_name]["buy"]

    @classmethod
    def find_all(cls):
        try:
            cls.collection.find({})
        except Exception as e:
            print("error find_all() for User models", e)

    @classmethod
    def insert_buy(cls, name, price, wallet_id):
        try:
            return cls.collection.insert_one(dict(name=name, price=price, wallet_id=wallet_id)).inserted_id
        except Exception as e:
            print("error find_all() for User models", e)

    @classmethod
    def delete_buy(cls, _id):
        try:
            query = {"_id": ObjectId(_id)}
            return True if cls.collection.delete_one(filter=query).deleted_count > 0 else False
        except Exception as e:
            print("error find_all() for User models", e)
            return False
