from pymongo import MongoClient
from werkzeug.security import check_password_hash

from config.config import Config


class User:
    collection = MongoClient(Config.mongodb_connection_string)[Config.mongodb_db_name]["users"]

    @classmethod
    def find_all(cls):
        try:
            return cls.collection.find({})
        except Exception as e:
            print("error find_all() for User models", e)
            return []

    @classmethod
    def find_one_username(cls, username):
        try:
            query = {"username": username}
            result = cls.collection.find_one(query)
            if result:
                return result
            else:
                return None
        except Exception as e:
            print("error find_all() for User models", e)
            return None

    @classmethod
    def insert_user(cls, username, password):
        try:
            inserted_id = cls.collection.insert_one(dict(username=username, password=password)).inserted_id
            return inserted_id
        except Exception as e:
            print("error find_all() for User models", e)
            return None

    @classmethod
    def exists_username(cls, username):
        try:
            count = cls.collection.count(dict(username=username))
            return True if count > 0 else False
        except Exception as e:
            print("error find_all() for User models", e)
            return None

    @classmethod
    def authentication_user(cls, username, password):
        try:
            user = cls.collection.find_one({"username": username})
            if user:
                user_username = user.get("username")
                user_password = user.get("password")

                correct_password = check_password_hash(user_password, password)
                if correct_password and username == user_username:
                    return True
            return False

        except Exception as e:
            print("error find_all() for User models", e)
            return False
