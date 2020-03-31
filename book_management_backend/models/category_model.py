from pymongo import MongoClient

from config.config import Config


class Category:
    collection = MongoClient(Config.mongodb_connection_string)[Config.mongodb_db_name]["category"]

    @classmethod
    def find_all(cls):
        try:
            cls.collection.find({})
        except Exception as e:
            print("error find_all() for User models", e)

    @classmethod
    def insert_user(cls, username, password):
        try:
            result = cls.collection.insert_one(dict(username=username, password=password))
            return result.count()
        except Exception as e:
            print("error find_all() for User models", e)
            return None
