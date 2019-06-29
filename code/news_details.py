import sqlite3
from flask_restful import Resource


class NewsDetails(Resource):

    # def __init__(self, _id, author, title, description, url, publishedAt, content, sourceId, categoryId):
    #     # super(, self).__init__()
    #     self.id = _id
    #     self.author = author
    #     self.title = title
    #     self.description = description
    #     self.url = url
    #     self.publishedAt = publishedAt
    #     self.content = content
    #     self.sourceId = sourceId
    #     self.categoryId = categoryId

    def get(self, id):
        connection = sqlite3.connect('news_db.db')
        cursor = connection.cursor()

        query = "SELECT * FROM news_details WHERE id=(?) "
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'news': {'id': row[0], 'author': row[1], 'title': row[2], 'description': row[3], 'url': row[4], 'publishedAt': row[5], 'content': row[6], 'sourceId': row[7], 'categoryId': row[8] }}
        return {'message': 'No source found'}, 404