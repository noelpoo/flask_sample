from flask import Flask
from flask_restful import Resource, Api

from common import GET_DAILY_LOGIN

app = Flask(__name__)
api = Api(app)


class DailyLogin(Resource):

    def get(self):
        return GET_DAILY_LOGIN, 200

    def post(self):
        return {
            'code': 429,
            'message': 'servers are busy right now, please try again later'
        }, 429


api.add_resource(DailyLogin, '/user/daily-login')


if __name__ == '__main__':
    app.run(debug=True, port=5000)


