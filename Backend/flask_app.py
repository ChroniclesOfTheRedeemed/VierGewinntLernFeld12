# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import CORS, cross_origin

from V4State import Status4G
from ViergewinntManager import GameManagement, game_manager
from user_management import UserManagement, user_manager

app = Flask(__name__)
CORS(app)


class Api:

    class Url:
        create_user = "/create_user"
        login = "/login"
        logout = "/logout"
        get_profile = "/get_profile"
        state = "/state"
        move = "/move"
        request_game = "/request_game"

    class Json:
        username = "username"
        password = "password"
        move = "coloumnNumber"
        token = "token"
        match_type = "match_type"
        status_name = "status"
        match_type_solo = "solo"
        player1turn = "player1turn"
        game_field = "game_field"
        player1 = "player1"
        player2 = "player2"
        game_finish = "game_state"


class BadRequestException(Exception):
    pass


@app.route(Api.Url.create_user, methods=['POST'])
@cross_origin()
def create_user():
    validation, properties = validate_request([Api.Json.username, Api.Json.password], request)
    if validation == "ok":

        status, result = user_manager.add_user(*properties)
        response = {
            Api.Json.token: result,
            Api.Json.status_name: status
        }

        # response.headers.add('Access-Control-Allow-Origin', '*')
        return jsonify(response)


@app.route(Api.Url.login, methods=['POST'])
@cross_origin()
def login():
    validation, properties = validate_request([Api.Json.username, Api.Json.password], request)
    if validation == "ok":
        status, result = user_manager.login(*properties)

        response = {
            Api.Json.token: result,
            Api.Json.status_name: status
        }
        return jsonify(response)


@app.route(Api.Url.logout, methods=['POST'])
@cross_origin()
def logout():
    validation, properties = validate_request([Api.Json.token], request)
    if validation == "ok":
        user_manager.logout(*properties)
        return jsonify({
            Api.Json.status_name: "ok"
        })


@app.route(Api.Url.get_profile, methods=['GET'])
@cross_origin()
def get_profile():
    validation, properties = validate_request([Api.Json.token, Api.Json.username], request)
    if validation == "ok":
        user_manager.get_user_profile(*properties)
        return jsonify({
            Api.Json.status_name: "ok"
        })


@app.route(Api.Url.state, methods=['GET'])
@cross_origin()
def get_game_state():
    validation, properties = validate_request([Api.Json.token], request)
    if validation == "ok":
        status, game_state, player1_name, player2_name = game_manager.fetch_state(*properties)
        response = create_game_state(game_state, player1_name, player2_name)
        response[Api.Json.status_name] = status
        return jsonify(response)

    else:
        return jsonify({
            Api.Json.status_name: validation
        })


@app.route(Api.Url.request_game, methods=['POST'])
@cross_origin()
def request_game():
    validation, properties = validate_request([Api.Json.token, Api.Json.match_type], request)
    if validation == "ok":
        r_token, r_match_type = properties
        response = {}
        if r_match_type == Api.Json.match_type_solo:
            status, game_state, player1_name, player2_name = game_manager.request_solo_game(r_token)
            response = create_game_state(game_state, player1_name, player2_name)
        else:
            status = "unknown match type"

        response[Api.Json.status_name] = status
        return jsonify(response)
    else:
        return jsonify({
            Api.Json.status_name: validation
        })


@app.route(Api.Url.move, methods=['POST'])
@cross_origin()
def move():
    validation, properties = validate_request([Api.Json.token, Api.Json.move], request)
    if validation == "ok":
        status, game_state, player1_name, player2_name = game_manager.make_move(*properties)
        response = create_game_state(game_state, player1_name, player2_name)
        response[Api.Json.status_name] = status
        return jsonify(response)
    else:
        return jsonify({
            Api.Json.status_name: validation
        })


def create_game_state(game_state: Status4G, player1_name, player2_name):
    return {
        Api.Json.player1turn: game_state.player1turn,
        Api.Json.game_field: create_game_field_response(game_state.SpielFeld),
        Api.Json.game_finish: game_state.result,
        Api.Json.player1: player1_name,
        Api.Json.player2: player2_name
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
    if Api.Json.token in args:
        if not user_manager.validate_token(props[args.index(Api.Json.token)]):
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
