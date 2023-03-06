class Api:

    class Url:
        base = "http://127.0.0.1:5000/"
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
        player_profile = "profile"
        ok = "ok"
        last_move = "last_move"


class BadRequestException(Exception):
    pass
