from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required

from news_source import NewsSourceById, NewsBySourceId, NewsBySourceName, NewsSources
from news_details import NewsDetails, News
from news_category import NewsCategoryById, NewsByCategoryId, NewsByCategoryName, NewsCategories

app = Flask(__name__)
app.secret_key = 'newsapi'
api = Api(app)


#API endpoints for getting news
api.add_resource(News, '/getAllNews')
api.add_resource(NewsCategories, '/getAllCategories')
api.add_resource(NewsSources, '/getAllSources')
api.add_resource(NewsDetails, '/getNewsById/<id>')
api.add_resource(NewsSourceById, '/getNewsSourceById/<id>')
api.add_resource(NewsBySourceId, '/getNewsBySourceId/<id>')
api.add_resource(NewsBySourceName, '/getNewsBySourceName/<name>')
api.add_resource(NewsCategoryById, '/getNewsCategoryById/<id>')
api.add_resource(NewsByCategoryId,  '/getNewsByCategoryId/<id>')
api.add_resource(NewsByCategoryName,  '/getNewsByCategoryName/<name>')

# api.add_resource(NewsDetails, '/getNewsByCategoryId/<int:categoryId>')

# run the app in  the specified port
app.run(port=5000, debug = True)
