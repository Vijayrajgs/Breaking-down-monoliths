from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class Equal(Resource):
    def get(self, number_1, number_2):
        return True if number_1 == number_2 else False

api.add_resource(Equal, '/<int:number_1>/<int:number_2>')

if __name__ == '__main__':
    app.run(debug=True,port=5061,host="0.0.0.0")