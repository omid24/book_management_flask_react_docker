import os
from bson import ObjectId
from pymongo import MongoClient
from config.config import Config


# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ", os.environ['MONGODB_USERNAME'], os.environ['MONGODB_PASSWORD'], type(os.environ['MONGODB_PASSWORD']), os.environ['MONGODB_HOSTNAME'], os.environ['MONGODB_DATABASE'])
# collection_error = 'mongodb://' + str(os.environ['MONGODB_USERNAME']) + ':' + str(os.environ['MONGODB_PASSWORD']) + '@' + str(os.environ['MONGODB_HOSTNAME']) + ':27017/' + str(os.environ['MONGODB_DATABASE'])
# print("collection_error : ", collection_error)
# collection_ok = MongoClient(Config.mongodb_connection_string)[Config.mongodb_db_name]["wallet"]
# print("collection_ok : ", collection_ok)
class Wallet:
    collection = MongoClient('mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ":27017/")[os.environ['MONGODB_DATABASE']]["wallet"]
    @classmethod
    def insert_wallet(cls, name, budget_amount, account_number, user_id):
        try:
            inserted_id = cls.collection.insert_one(
                dict(name=name, budget_amount=budget_amount, account_number=account_number,
                     user_id=ObjectId(user_id))).inserted_id
            return inserted_id
        except Exception as e:
            print("error find_all() for User models", e)
            return None

    @classmethod
    def insert_wallet_without_user(cls, name, budget_amount, account_number):
        try:
            inserted_id = cls.collection.insert_one(
                dict(name=name, budget_amount=budget_amount, account_number=account_number)).inserted_id
            return inserted_id
        except Exception as e:
            print("error find_all() for User models", e)
            return None

    @classmethod
    def exist_wallet_user(cls, user_id):
        try:
            count = cls.collection.count(dict(user_id=ObjectId(user_id)))
            return True if count > 0 else False
        except Exception as e:
            print("error find_all() for User models", e)
            return True

    @classmethod
    def find_one_wallet(cls, user_id):
        try:
            query = {"user_id": ObjectId(user_id)}
            result = cls.collection.find_one(query)
            if result:
                return result
            else:
                return None
        except Exception as e:
            print("error find_all() for User models", e)
            return None

    @classmethod
    def update_budget_amount(cls, user_id, amount):
        try:
            query = {"user_id": user_id}
            update = {"$set": {"budget_amount": amount}}
            result = cls.collection.find_one_and_update(query, update)
            if result:
                return result
            else:
                return None
        except Exception as e:
            print("error find_all() for User models", e)
            return None


    @classmethod
    def find_all(cls):
        docs = []
        try:

            results = cls.collection.find({}).sort("_id", -1)
            print(results)
            if results:
                for cursor in results:
                    _id = cursor.get("_id")
                    if isinstance(_id, ObjectId):
                        cursor["_id"] = str(_id)
                    docs.append(cursor)
                return docs
            else:
                return docs
        except Exception as e:
            print("error find_all() for User models", e)
            return docs

    @classmethod
    def delete_id(cls, _id):
        try:
            result = cls.collection.delete_one({"_id": ObjectId(_id)})
            return result.deleted_count
        except Exception as e:
            print("error find_all() for User models", e)
            return None