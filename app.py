import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required
from flask_sqlalchemy import SQLAlchemy


from resources.news_source import NewsSourceById, NewsBySourceId, NewsBySourceName, NewsSources
from resources.news_details import NewsDetails, News
from resources.news_category import NewsCategoryById, NewsByCategoryId, NewsByCategoryName, NewsCategories

app = Flask(__name__)

# app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'newsapi'
db = SQLAlchemy(app)
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
# if __name__ == '__main__':
#     from db import db
#     db.init_app(app)

#     if app.config['DEBUG']:
#         @app.before_first_request
#         def create_tables():
#             db.create_all()

app.run(port=5050, debug=True)
