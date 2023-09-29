import data

def test():
    
    # data preparation
    fields_player_1 = {
        "name_player" : "deko",
        "team_player" : "gg_s_0",
        "score_player" : 27,
        "data_role" : "what is it"
    }

    fields_player_2 = {
        "name_player" : "interz",
        "team_player" : "c9",
        "score_player" : 23,
        "data_role" : "what again"
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

    data.info_stack.register("players_id", "001", fields_player_1)
    data.info_stack.register("players_id", "002", fields_player_2)
    data.info_stack.register("teams_id", "1", fields_team)
    data.info_stack.register("polygons_id", "001", fields_polygon)
    data.info_stack.register("servers_id", "1", fields_server)

    # check pulling registered fields - OK

    pull_check = data.info_stack.pull("players_id", "001", ["name_player", "team_player"])
    print(pull_check)
    pull_check = data.info_stack.pull("players_id", "002", ["name_player", "team_player"])
    print(pull_check)
    pull_check = data.info_stack.pull("teams_id", "1", ["team_score"])
    print(pull_check)
    pull_check = data.info_stack.pull("polygons_id", "001", ["x", "y", "z"])
    print(pull_check)
    pull_check = data.info_stack.pull("servers_id", "1", ["adress"])
    print(pull_check)
    print()

    # request examples
    request_1 = {
    "players_info": { "players_id": ["001", "002"], "fields": ["name_player", "team_player", "score_player", "data_role"]},
    "polygons_info": {"polygons_id": ["001"], "fields": ["x", "y", "z"]},
    "teams_info": {"teams_id": ["1"], "fields": ["team_members", "team_score"]}, 
    "servers_info": {"servers_id": ["1"], "fields": ["adress", "ping"]}
    }

    # parsing
    process = data.parser()
    response_1 = process.parse(request_1)
    print("request = ", request_1)
    print()
    print("response = ", response_1)

test()