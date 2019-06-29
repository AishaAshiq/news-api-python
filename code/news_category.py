import sqlite3
from flask_restful import Resource, Api
from flask import Flask


class NewsCategory(Resource):
    # def __init__(self, _id, categoryName):
    #     self.id = _id
    #     self.categoryName = categoryName

    # function to get the news category based on the id
    def get(self, id):

        #connect to sqlite database
        connection = sqlite3.connect('news_db.db')
        cursor = connection.cursor()
        
        #query to select the category based on the id
        query = "SELECT * FROM news_category WHERE id = ?"
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        connection.close()

        #check for null and return the fetched values from database to the API
        if row:
            return {'newsCategory': {'id': row[0], 'categoryName': row[1]}}
        return {'message': 'No category found for the given ID'}, 404

class NewsByCategory(Resource):

    # function to get the news based on the given category ID
    def get(self, id):

        #connect to sqlite database
        connection = sqlite3.connect('news_db.db')
        cursor = connection.cursor()

        #query to fetch the news from the table for the given category id
        query = "SELECT * FROM news_details WHERE categoryId = (?)"
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
        return {'message': 'No news found for the given category ID'}, 404
