from flask import Flask, jsonify, request
from mysql import MySqlCommand
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

mysqlCommand = MySqlCommand()
mysqlCommand.connectionMysql()


#test
@app.route('/')
def hello_world():
    return "hello world"


#Python
@app.route('/api/python', methods=['GET'])
def get():
    data = {'message': "This is A Get Request"}
    res = mysqlCommand.QueryData("shixi")
    return jsonify(res)


@app.route('/post', methods=['POST'])
def postTest():
    data = request.get_json()
    response = {"message": "this isPOst", "data": data}

    return jsonify(response)


# @app.route('/python', methods=['GET'])
# def getPythonData():

#     data = {"code": "200", "message": "ok"}
#     return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
