# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import CORS, cross_origin

from V4State import Status4G
from ViergewinntManager import GameManagement, game_manager
from user_management import UserManagement, user_manager

app = Flask(__name__)
CORS(app)


class Response:

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


class BadRequestException(Exception):
    pass


@app.route('/create_user', methods=['POST'])
@cross_origin()
def create_user():
    validation, properties = validate_request([Response.email, Response.password], request)
    if validation == "ok":

        status, result = user_manager.add_user(*properties)
        response = {
            Response.token: result,
            Response.status_name: status
        }

        # response.headers.add('Access-Control-Allow-Origin', '*')
        return jsonify(response)


@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    validation, properties = validate_request([Response.email, Response.password], request)
    if validation == "ok":
        status, result = user_manager.login(*properties)

        response = {
            Response.token: result,
            Response.status_name: status
        }
        return jsonify(response)


@app.route('/logout', methods=['POST'])
@cross_origin()
def logout():
    validation, properties = validate_request([Response.token], request)
    if validation == "ok":
        user_manager.logout(*properties)
        return jsonify({
            Response.status_name: "ok"
        })


@app.route('/get_profile', methods=['GET'])
@cross_origin()
def get_profile():
    validation, properties = validate_request([Response.token, Response.email], request)
    if validation == "ok":
        user_manager.get_user_profile(*properties)
        return jsonify({
            Response.status_name: "ok"
        })


@app.route('/state', methods=['GET'])
@cross_origin()
def get_game_state():
    validation, properties = validate_request([Response.token], request)
    if validation == "ok":
        status, game_state, player1_name, player2_name = game_manager.fetch_state(*properties)
        response = create_game_state(game_state, player1_name, player2_name)
        response[Response.status_name] = status
        return jsonify(response)

    else:
        return jsonify({
            Response.status_name: validation
        })


@app.route('/request_game', methods=['POST'])
@cross_origin()
def request_game():
    validation, properties = validate_request([Response.token, Response.match_type], request)
    if validation == "ok":
        r_token, r_match_type = properties
        response = {}
        if r_match_type == Response.match_type_solo:
            status, game_state, player1_name, player2_name = game_manager.request_solo_game(r_token)
            response = create_game_state(game_state, player1_name, player2_name)
        else:
            status = "unknown match type"

        response[Response.status_name] = status
        return jsonify(response)
    else:
        return jsonify({
            Response.status_name: validation
        })


@app.route('/move', methods=['POST'])
@cross_origin()
def move():
    validation, properties = validate_request([Response.token, Response.json_move], request)
    if validation == "ok":
        status, game_state, player1_name, player2_name = game_manager.make_move(*properties)
        response = create_game_state(game_state, player1_name, player2_name)
        response[Response.status_name] = status
        return jsonify(response)
    else:
        return jsonify({
            Response.status_name: validation
        })


def create_game_state(game_state: Status4G, player1_name, player2_name):
    return {
        Response.json_player1turn: game_state.player1turn,
        Response.json_game_field: create_game_field_response(game_state.SpielFeld),
        Response.json_game_finish: game_state.result,
        Response.json_player1: player1_name,
        Response.json_player2: player2_name
    }


def create_game_field_response(game_field):
    result = {}
    for index, coloumn in enumerate(game_field):
        result["coloumn_" + str(index)] = coloumn
    return result


def validate_request(args: list, request_to_validate):
    json = request_to_validate.json
    props = find_properties_in_answer(args, json)
    status = "ok"
    if Response.token in args:
        if not user_manager.validate_token(props[args.index(Response.token)]):
            status = "bad request"
    if not props:
        status = "bad request"
    return status, props


def find_properties_in_answer(args: list, json):
    properties = []
    for arg in args:
        if arg in json:
            properties.append(json[arg])
        else:
            properties = []
            break
    return tuple(properties) if len(properties) == len(args) else None


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
