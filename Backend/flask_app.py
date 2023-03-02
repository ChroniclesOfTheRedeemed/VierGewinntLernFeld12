# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import CORS, cross_origin

from ViergewinntManager import GameManagement, game_manager
from user_management import UserManagement, user_manager

app = Flask(__name__)
CORS(app)

email = "username"
password = "password"
move = "coloumnNumber"
option = "option"
token = "token"
match_type = "match_type"

match_type_solo = "solo"


@app.route('/create_user', methods=['POST'])
@cross_origin()
def create_user():
    if request.method == 'POST':
        x = request.json
        print(x)

        if email in x and password in x:
            result = user_manager.add_user(x[email], x[password])
        else:
            result = "bad request"
        if result == "invalid" or result == "bad request":
            response = {
                token: 0,
                "status": result
            }
        else:
            response = {
                token: result,
                "status": "ok"
            }
        # response.headers.add('Access-Control-Allow-Origin', '*')
        return jsonify(response)


@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    if request.method == 'POST':
        x = request.json
        print(x)

        if email in x and password in x:
            result = user_manager.login(x[email], x[password])
        else:
            result = "bad request"
        if result == "invalid" or result == "bad request":
            response = {
                token: 0,
                "status": result
            }
        else:
            response = {
                token: result,
                "status": "ok"
            }
        # response.headers.add('Access-Control-Allow-Origin', '*')
        return jsonify(response)


@app.route('/state', methods=['GET'])
@cross_origin()
def get_game_state():
    if request.method == 'GET':
        x = request.json
        print(x)
        if token in x:
            return user_manager.add_user(x[email], x[password])
        return "bad request"


@app.route('/request_game', methods=['POST'])
@cross_origin()
def request_game():
    if request.method == 'POST':
        x = request.json
        print(x)
        answer = "there has been an issue"
        if token in x and match_type in x:
            if x[match_type] == match_type_solo:
                answer = game_manager.request_game(x[token], x[match_type])

        return answer


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
