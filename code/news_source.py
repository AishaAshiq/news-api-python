import sqlite3
from flask_restful import Resource


class NewsSource(Resource):
    # def __init__(self, _id, name):
    #     self.id = _id
    #     self.name = name

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

    