import sqlite3
from flask_restful import Resource

class NewsSources(Resource):
    # function to get all news
    def get(self):

        #connect to sqlite database
        connection = sqlite3.connect('news_db.db')
        cursor = connection.cursor()

        #query to fetch the news from the table for the given category id
        query = "SELECT * FROM news_source"
        result = cursor.execute(query)
        # row = result.fetchall()

        #save the fetched rows in a list
        sources = []
        for n in result:
            sources.append({'id': n[0], 'sourceName': n[1]})
        connection.close()

        #check for null values and return the news list
        if sources:
            return {'sources': sources}
        return {'message': 'No source found'}, 404

class NewsSourceById(Resource):
    # function to get the news source based on the id
    def get(self, id):

        #connect to sqlite database
        connection = sqlite3.connect('news_db.db')
        cursor = connection.cursor()

        #query to select the category based on the id
        query = "SELECT * FROM news_source WHERE id=(?) "
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        connection.close()

        #check for null and return the fetched values from database to the API
        if row:
            return {'source': {'id': row[0], 'name': row[1] }}
        return {'message': 'No source found for the given ID'}, 404

class NewsBySourceId(Resource):
    # function to get the news based on the given source ID
    def get(self, id):

        #connect to sqlite database
        connection = sqlite3.connect('news_db.db')
        cursor = connection.cursor()

        #query to fetch the news from the table for the given source id
        query = "SELECT * FROM news_details WHERE sourceId = (?)"
        result = cursor.execute(query, (id,))
        # row = result.fetchall()

        #save the fetched rows in a list
        news = []
        for n in result:
            news.append({'id': n[0], 'author': n[1], 'title': n[2], 'description': n[3], 'url': n[4], 'publishedAt': n[5], 'content': n[6], 'sourceId': n[7], 'categoryId': n[8] })
        connection.close()

        #check for null values and return the news list
        if news:
            return {'news': news}
        return {'message': 'No news found for the given source ID'}, 404

class NewsBySourceName(Resource):
    # function to get the news based on the given category name
    def get(self, name):

        #connect to sqlite database
        connection = sqlite3.connect('news_db.db')
        cursor = connection.cursor()

        #query to fetch the news from the table for the given category name
        query = "SELECT * FROM news_details WHERE sourceId IN (SELECT id FROM news_source WHERE name = (?))"
        result = cursor.execute(query, (name,))
        # row = result.fetchall()

        #save the fetched rows in a list
        news = []
        for n in result:
            news.append({'id': n[0], 'author': n[1], 'title': n[2], 'description': n[3], 'url': n[4], 'publishedAt': n[5], 'content': n[6], 'sourceId': n[7], 'categoryId': n[8] })
        connection.close()

        #check for null values and return the news list
        if news:
            return {'news': news}
        return {'message': 'No news found for the given source Name'}, 404



    