import data

def test():
    # creating fields for each type of entity
    fields_for_players = []

    ##### player's ID RANGE: team_1: [1 TO 5], team_2: [6 to 10]
    for _id in range(5):
        fields_for_players.append({
            "name_player" : str(_id),
            "team_player" : "team_1",
            "score_player" : "example",
            "data_role" : "smth"
        })
    for _id in range(5, 10):
        fields_for_players.append({
            "name_player" : str(_id),
            "team_player" : "team_2",
            "score_player" : "example",
            "data_role" : "smth"
        })

    print(fields_for_players)
    print()

    ##### TEAMS 
    team_1_fields = {
        "team_members" : ["1", "2", "3", "4", "5"],
        "team_score" : 30
    }

    team_2_fields = {
        "team_members" : ["6", "7", "8", "9", "10"],
        "team_score" : 25
    }

    ##### POLYGONS (independent for now)
    fields_polygon = []

    for i in range(20):
        fields_polygon.append({"x" : i, "y" : i+1, "z" : i+2})


    ##### SERVERS (2 for now)
    server_1_fields = {
        "adress" : "Stockholm",
        "ping" : 17
    }    

    server_2_fields = {
        "adress" : "Chista",
        "ping" : 17
    }

    # data registration

    ##### PLAYERS
    for _id in range(10):
        data.InfoStack.register("players_id", str(_id), fields_for_players[_id])


    ##### TEAMS
    

    ##### POLYGONS
    
    ##### SERVERS 
    
    # requests
    request_1 = {
    "players_info": { "players_id": ["1", "7"], "fields": ["name_player", "team_player", "score_player", "data_role"]},
    #"polygons_info": {"polygons_id": [5, 9, 17], "fields": ["x", "y", "z"]},
    #"teams_info": {"teams_id": ["1"], "fields": ["team_members", "team_score"]}, 
    #"servers_info": {"servers_id": ["1"], "fields": ["adress", "ping"]}
    }
    request_2 = {
    "players_info": { "players_id": ["11", "5"], "fields": ["name_player", "team_player", "score_player", "data_role"]},
    #"polygons_info": {"polygons_id": [5, 9, 17], "fields": ["x", "y", "z"]},
    #"teams_info": {"teams_id": ["1"], "fields": ["team_members", "team_score"]}, 
    #"servers_info": {"servers_id": ["1"], "fields": ["adress", "ping"]}
    }

    # parsing
    test = data.Parser()
    
    print("response 1 = ", test.parse(request_1))
    print()

    print("response 2 = ", test.parse(request_2))
    print()
    pass

test()