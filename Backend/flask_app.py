# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import CORS, cross_origin

from V4State import Status4G
from ViergewinntManager import GameManagement, game_manager
from user_management import UserManagement, user_manager

app = Flask(__name__)
CORS(app)

email = "username"
password = "password"
json_move = "coloumnNumber"
option = "option"
token = "token"
match_type = "match_type"
status_name = "status"
match_type_solo = "solo"
json_player1turn = "player1turn"
json_game_field = "game_field"
json_player1 = "player1"
json_player2 = "player2"
json_game_finish = "game_state"


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
        if result == "invalid" or result == "bad request" or result == "user already exists":
            response = {
                token: "0",
                status_name: result
            }
        else:
            response = {
                token: result,
                status_name: "ok"
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
                token: "0",
                status_name: result
            }
        else:
            response = {
                token: result,
                status_name: "ok"
            }
        return jsonify(response)


@app.route('/logout', methods=['POST'])
@cross_origin()
def logout():
    if request.method == 'POST':
        x = request.json
        print(x)

        if token in x:
            user_manager.logout(x[token])

        return jsonify({
            status_name: "ok"
        })


@app.route('/state', methods=['GET'])
@cross_origin()
def get_game_state():
    if request.method == 'GET':
        x = request.json
        print(x)
        answer = "there has been an issue"
        if token in x:
            status, game_state, player1_name, player2_name = game_manager.fetch_state(x[token])
            response = create_game_state(game_state, player1_name, player2_name)
        else:
            status = "bad request"
        if status == "ok":
            response[status_name] = status
            return jsonify(response)
        else:
            return jsonify({
                status_name: status
            })


@app.route('/request_game', methods=['POST'])
@cross_origin()
def request_game():
    if request.method == 'POST':
        x = request.json
        print(x)
        answer = "there has been an issue"
        if token in x and match_type in x:
            if x[match_type] == match_type_solo:
                status, game_state, player1_name, player2_name = game_manager.request_solo_game(x[token])
                response = create_game_state(game_state, player1_name, player2_name)
            else:
                status = "unkown match type"
        else:
            status = "bad request"
        if status == "ok":
            response[status_name] = status
            return jsonify(response)
        else:
            return jsonify({
                status_name: status
            })


@app.route('/move', methods=['POST'])
@cross_origin()
def move():
    if request.method == 'POST':
        x = request.json
        print(x)
        answer = "there has been an issue"
        if token in x and json_move in x:
            status, game_state, player1_name, player2_name = game_manager.make_move(x[token], x[json_move])
            response = create_game_state(game_state, player1_name, player2_name)
        else:
            status = "bad request"
        if status == "ok":
            response[status_name] = status
            return jsonify(response)
        else:
            return jsonify({
                status_name: status
            })


def create_game_state(game_state: Status4G, player1_name, player2_name):
    return {
        json_player1turn: game_state.player1turn,
        json_game_field: create_game_field_response(game_state.SpielFeld),
        json_game_finish: game_state.result,
        json_player1: player1_name,
        json_player2: player2_name
    }


def create_game_field_response(game_field):
    result = {}
    for index, coloumn in enumerate(game_field):
        result["coloumn_" + str(index)] = coloumn
    return result


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
