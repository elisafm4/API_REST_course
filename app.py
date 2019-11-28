from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'# database is on the same directory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # don¡t track changes in the sqlalchemy
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all() # if the db set on sqlite doesn't exists, create it

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    from db import db # better here
    db.init_app(app)
    app.run(port=5000, debug=True)  # important to mention debug=True
