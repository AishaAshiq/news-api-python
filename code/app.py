from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required

from news_source import NewsSource
from news_details import NewsDetails
from news_category import NewsCategory, NewsByCategory

app = Flask(__name__)
app.secret_key = 'newsapi'
api = Api(app)


#API endpoints for getting news
api.add_resource(NewsDetails, '/getNewsById/<id>')
api.add_resource(NewsSource, '/getNewsSourceById/<id>')
api.add_resource(NewsCategory, '/getNewsCategoryById/<id>')
api.add_resource(NewsByCategory,  '/getNewsByCategoryId/<id>')
# api.add_resource(NewsDetails, '/getNewsByCategoryId/<int:categoryId>')

# run the app in  the specified port
app.run(port=5000, debug = True)
