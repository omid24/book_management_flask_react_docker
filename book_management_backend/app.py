import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_pymongo import PyMongo
from api.buy_api import BuyController
from config.config import Config
from api.login_user_api import LoginUser
from api.signup_user_api import SignUpUser
from api.wallet_controller_api import WalletController
from flask_jwt_extended import JWTManager
from config.config import Config

app = Flask(__name__)
# app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
# mongo = PyMongo(app)
# db = mongo.db
# Config.db_connection = db

CORS(app)
app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = Config.JWT_ACCESS_TOKEN_EXPIRES
api = Api(app)
jwt = JWTManager(app)


"""
Run Debug Mode and Auto Reload In PowerShell:
    1 - Open PowerShell with administrator
    2 - $env:FLASK_ENV='development'
    3 - flask run

Run Debug Mode and Auto Reload In CMD:
    1 - Open PowerShell with administrator
    2 - set FLASK_ENV=development
    3 - flask run

# => Reference: https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart
"""

api.add_resource(SignUpUser, '/users/signup')
api.add_resource(LoginUser, '/users/login')
api.add_resource(WalletController, '/users/wallet')
api.add_resource(BuyController, '/users/buy')

if __name__ == '__main__':
    app.run()
