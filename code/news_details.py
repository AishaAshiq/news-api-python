import sqlite3
from flask_restful import Resource


class NewsDetails(Resource):

    # function to get the news based on the id    
    def get(self, id):

        #connect to sqlite database
        connection = sqlite3.connect('news_db.db')
        cursor = connection.cursor()

        #query to select the category based on the id
        query = "SELECT * FROM news_details WHERE id=(?) "
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        connection.close()

        #check for null and return the fetched values from database to the API
        if row:
            return {'news': {'id': row[0], 'author': row[1], 'title': row[2], 'description': row[3], 'url': row[4], 'publishedAt': row[5], 'content': row[6], 'sourceId': row[7], 'categoryId': row[8] }}
        return {'message': 'No news found for the given ID'}, 404

    