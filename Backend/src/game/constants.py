class Api:

    class Url:
        base = "http://127.0.0.1:5000/"
        create_user = "/create_user"
        login = "/login"
        logout = "/logout"
        get_profile = "/get_profile"
        state = "/state"
        move = "/move"
        challenge = "/request_game"
        fetch_challengers = "/fetch_challengers"
        forfeit = "/forfeit_game"
        get_online_list = "/fetch_online_users"

    class Json:
        username = "username"
        password = "password"
        move = "coloumnNumber"
        token = "token"
        match_type = "match_type"
        status_name = "status"
        match_type_solo = "solo"
        match_made = "match"
        player1turn = "player1turn"
        game_field = "game_field"
        player1 = "player1"
        player2 = "player2"
        game_finish = "game_state"
        player_profile = "profile"
        ok = "ok"
        last_move = "last_move"
        challengers = "challengers"
        online_player_list = "online_player_list"


class BadRequestException(Exception):
    pass
