import data

def test():
    
    # data preparation
    fields_player = {
        "name_player" : "deko",
        "team_player" : "gg_s_0",
        "score_player" : 27,
        "data_role" : "what is it"
    }

    fields_team = {
        "team_members" : "deko",
        "team_score" : 13
    }

    fields_polygon = {
        "x" : 3,
        "y" : 2,
        "z" : 5
    }

    fields_server = {
        "adress" : "Stockholm",
        "ping" : 17
    }

    # filling info_stack

    data.info_stack.register("player_id", "001", fields_player)
    data.info_stack.register("team_id", "1", fields_team)
    data.info_stack.register("polygon_id", "001", fields_polygon)
    data.info_stack.register("server_id", "1", fields_server)

    # check pulling registered fields - OK

    pull_check = data.info_stack.pull("player_id", "001", ["name_player", "team_player"])
    print(pull_check)
    pull_check = data.info_stack.pull("team_id", "1", ["team_score"])
    print(pull_check)
    pull_check = data.info_stack.pull("polygon_id", "001", ["x", "y", "z"])
    print(pull_check)
    pull_check = data.info_stack.pull("server_id", "1", ["adress"])
    print(pull_check)
    print()

    # request examples
    request_1 = {
    "players_info": { "player_id": "001", "fields": ["name_player", "team_player", "score_player", "data_role"]},
    "polygons_info": {"polygon_id": "001", "fields": ["x", "y", "z"]},
    "teams_info": {"team_id": "1", "fields": ["team_members", "team_score"]}, 
    "servers_info": {"server_id": "1", "fields": ["adress", "ping"]}
    }

    # parsing
    process = data.parser()
    response_1 = process.parse(request_1)
    print("request = ", request_1)
    print()
    print("response = ", response_1)

test()