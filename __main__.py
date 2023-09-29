import data

def test():
    
    # data preparation
    ## player's fields
    players_fields = list()

    for i in range(5):
        players_fields.append({
            "name_player" : i,
            "team_player" : 1,
            "score_player" : 10 - i,
            "data_role" : "smth"
        })

    for i in range(5):
        players_fields.append({
            "name_player" : i+5,
            "team_player" : 2,
            "score_player" : 10 - i,
            "data_role" : "smth"
        })    
    ## team's fields

    team_fields_1 = {
        "team_members" : [0, 1, 2, 3, 4],
        "team_score" : 30
    }

    team_fields_2 = {
        "team_members" : [5, 6, 7, 8, 9],
        "team_score" : 25
    }

    ## polygon's fields
    fields_polygon = []

    for i in range(20):
        fields_polygon.append({"x" : i, "y" : i+1, "z" : i+2})

    ## server's fields
    fields_server = {
        "adress" : "Stockholm",
        "ping" : 17
    }

    # filling info_stack
    p_id = 0
    for player in players_fields:
        data.info_stack.register("players_id", str(p_id), player)
        p_id += 1

    p_id = 0
    for polygon in fields_polygon:
        data.info_stack.register("polygons_id", str(p_id), polygon)
        p_id += 1

    # check pulling registered fields - OK
    p_id = 0
    players = []
    for i in range(10):
        players.append(data.info_stack.pull("players_id", str(i), ["name_player", "team_player"]))

    print("PULLED PLAYERS = ", players)
    print()

    polygons = []
    for i in range(20):
        polygons.append(data.info_stack.pull("polygons_id",  str(i), ["x", "y"]))
    print("PULLED POLYGONS = ", polygons)

    # request examples
    
    print()

    request_1 = {
    "players_info": { "players_id": ["0", "1"], "fields": ["name_player", "team_player", "score_player", "data_role"]},
    "polygons_info": {"polygons_id": ["0", "3"], "fields": ["x", "y", "z"]},
    #"teams_info": {"teams_id": ["1"], "fields": ["team_members", "team_score"]}, 
    #"servers_info": {"servers_id": ["1"], "fields": ["adress", "ping"]}
    }

    # parsing
    process = data.parser()
    response_1 = process.parse(request_1)
    print("request = ", request_1)
    print()
    print("response = ", response_1)
    print()

test()