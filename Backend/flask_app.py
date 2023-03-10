# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from V4State import Status4G
from ViergewinntManager import game_manager
from constants import Api
from user_management import user_manager

app = Flask(__name__)
CORS(app)


@app.route(Api.Url.create_user, methods=['POST'])
@cross_origin()
def create_user():
    validation, properties = validate_request([Api.Json.username, Api.Json.password], request)
    if validation == Api.Json.ok:
        status, result = user_manager.add_user(*properties)
        response = {
            Api.Json.token: result,
            Api.Json.status_name: status
        }
        return jsonify(response)


@app.route(Api.Url.login, methods=['POST'])
@cross_origin()
def login():
    validation, properties = validate_request([Api.Json.username, Api.Json.password], request)
    if validation == Api.Json.ok:
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
    if validation == Api.Json.ok:
        status = user_manager.logout(*properties)
        return jsonify({
            Api.Json.status_name: status
        })


@app.route(Api.Url.get_profile, methods=['GET'])
@cross_origin()
def get_profile():
    validation, properties = validate_request([Api.Json.token, Api.Json.username], request)
    if validation == Api.Json.ok:
        status, profile = user_manager.get_user_profile(*properties)
        return jsonify({
            Api.Json.status_name: status,
            Api.Json.player_profile: profile
        })


@app.route(Api.Url.state, methods=['GET'])
@cross_origin()
def get_game_state():
    validation, properties = validate_request([Api.Json.token], request)
    if validation == Api.Json.ok:
        status, game_state, player1_name, player2_name = game_manager.fetch_state(*properties)
        response = create_game_state(game_state, player1_name, player2_name)
        response[Api.Json.status_name] = status
        return jsonify(response)

    else:
        return jsonify({
            Api.Json.status_name: validation
        })


@app.route(Api.Url.challenge, methods=['POST'])
@cross_origin()
def request_game():
    validation, properties = validate_request([Api.Json.token, Api.Json.username], request)
    if validation == Api.Json.ok:
        r_token, r_username = properties
        response = {}
        user = user_manager.sessions[r_token]
        if r_match_type == Api.Json.match_type_solo:
            user = user_manager.sessions[r_token]
            status, game_state, player1_name, player2_name = game_manager.start_game(user, user)
            # response = create_game_state(game_state, player1_name, player2_name)
        elif r_match_type == Api.Json.match_made:
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


@app.route(Api.Url.fetch_challenges, methods=['GET'])
@cross_origin()
def fetch_challenges():
    validation, properties = validate_request([Api.Json.token], request)
    if validation == Api.Json.ok:
        status, challenges = game_manager.fetch_challenges(*properties)
        if status == Api.Json.ok:
            response = challenges
            response[Api.Json.status_name] = status
        else:
            response = {Api.Json.status_name: status}
    else:
        response = {Api.Json.status_name: validation}
    return jsonify(response)


@app.route(Api.Url.move, methods=['POST'])
@cross_origin()
def move():
    validation, properties = validate_request([Api.Json.token, Api.Json.move], request)
    if validation == Api.Json.ok:
        status, game_state, player1_name, player2_name = game_manager.make_move(*properties)
        if status == Api.Json.ok:
            response = create_game_state(game_state, player1_name, player2_name)
            response[Api.Json.status_name] = status
        else:
            response = {Api.Json.status_name: status}
    else:
        response = {Api.Json.status_name: validation}
    return jsonify(response)


@app.route(Api.Url.forfeit, methods=['POST'])
@cross_origin()
def forfeit():
    validation, properties = validate_request([Api.Json.token], request)
    if validation == Api.Json.ok:
        status = game_manager.forfeit_match(*properties)
        response = {Api.Json.status_name: status}
    else:
        response = {Api.Json.status_name: validation}
    return jsonify(response)


def create_game_state(game_state: Status4G, player1_name, player2_name):
    return {
        Api.Json.player1turn: game_state.player1turn,
        Api.Json.game_field: create_game_field_response(game_state.SpielFeld),
        Api.Json.game_finish: game_state.result,
        Api.Json.player1: player1_name,
        Api.Json.player2: player2_name,
        Api.Json.last_move: game_state.last_move
    }


def create_game_field_response(game_field):
    result = {}
    for index, coloumn in enumerate(game_field):
        result["coloumn_" + str(index)] = coloumn
    return result


def validate_request(args: list, request_to_validate):
    json = request_to_validate.json
    props = find_properties_in_answer(args, json)
    status = Api.Json.ok
    if not props:
        status = "bad request"
    elif Api.Json.token in args:
        if not user_manager.validate_token(props[args.index(Api.Json.token)]):
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
