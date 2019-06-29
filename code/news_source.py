import sqlite3
from flask_restful import Resource


class NewsSource(Resource):
    # def __init__(self, _id, name):
    #     self.id = _id
    #     self.name = name

    def get(self, id):
        connection = sqlite3.connect('news_db.db')
        cursor = connection.cursor()

        query = "SELECT * FROM news_source WHERE id=(?) "
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'source': {'id': row[0], 'name': row[1] }}
        return {'message': 'No source found'}, 404

    # def getid(self):
    #     connection = sqlite3.connect('news_db.db')
    #     cursor = connection.cursor()

    #     query = "SELECT * FROM news_source"
    #     result = cursor.execute(query)
    #     rows = result.fetchmany()
    #     connection.close()

    #     if rows:
    #         for r in rows:
    #             return {'items': rows[r] }
    #     return {'message': 'No items found'}, 404


# Api.add_resource(NewsSource, '/sources')
