from flask import Flask
from flask_restful import Api
# from flask_jwt import JWT
from flask_jwt import JWT, jwt_required

from news_source import NewsSource
from news_details import NewsDetails
# from news_category import NewsCategory

app = Flask(__name__)
app.secret_key = 'newsapi'
api = Api(app)

# jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(NewsDetails, '/news/<id>')
api.add_resource(NewsSource, '/newssource/<id>')
# api.add_resource(NewsSource, '/sources')
# api.add_resource(NewsCategory, '/newscategories')

app.run(port=5000, debug = True)
