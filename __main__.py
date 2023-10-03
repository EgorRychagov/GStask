import data

def regTest():
    # PLAYERS
    players_fields = []

    for _id in range(5):
        players_fields.append({
            "name_player" : str(_id),
            "team_player" : "team_1",
            "score_player" : "example",
            "data_role" : "smth"
        })
    for _id in range(5, 10):
        players_fields.append({
            "name_player" : str(_id),
            "team_player" : "team_2",
            "score_player" : "example",
            "data_role" : "smth"
        })

    for _id in range(10):
        data.InfoStack.register(players_fields[_id], id_name = "players_id", id_inst = str(_id))

    # TEAMS 
    team_1_fields = {
        "team_members" : ["1", "2", "3", "4", "5"],
        "team_score" : 30
    }

    team_2_fields = {
        "team_members" : ["6", "7", "8", "9", "10"],
        "team_score" : 25
    }

    data.InfoStack.register(team_1_fields, id_name = "teams_id", id_inst = "team_1")
    data.InfoStack.register(team_2_fields, id_name = "teams_id", id_inst = "team_2")

    # POLYGONS 
    polygon_fields = []

    for i in range(20):
        polygon_fields.append({"x" : i, "y" : i+1, "z" : i+2})

    for i in range(20):
        data.InfoStack.register(polygon_fields[i], id_name = "polygons_id", id_inst = i)

    # SERVERS 
    server_fields = {
        "adress" : "Stockholm",
        "capacity" : 10,
        "workload" : 7
    }    

    data.InfoStack.register(server_fields, id_name = "servers_id")

    print("\nData was registered\n")

def pullTest():
    print("PULLING:\n")

    print("1) Existing data / all fields: \n")
    print("player = ", data.InfoStack.pull(["name_player", "score_player", "team_player", "data_role"], id_name = "players_id", id_inst = "3"))
    print("team = ", data.InfoStack.pull(["team_members", "team_score"], id_name = "teams_id", id_inst = "team_1"))
    print("polygon = ", data.InfoStack.pull(["x", "y"], id_name = "polygons_id", id_inst = 2))
    print("server = ", data.InfoStack.pull(["adress", "workload"], id_name = "servers_id"), "\n")

    pass

def requestTest():

    request_1 = {
    "players_info": { "players_id": ["1", "7"], "fields": ["name_player", "team_player", "score_player", "data_role"]},
    #"polygons_info": {"polygons_id": [5, 9, 17], "fields": ["x", "y", "z"]},
    #"teams_info": {"teams_id": ["1"], "fields": ["team_members", "team_score"]}, 
    "servers_info": {"fields": ["adress", "capacity"]}
    }
    request_2 = {
    "players_info": { "players_id": ["11", "5"], "fields": ["name_player", "team_player", "score_player", "data_role"]},
    #"polygons_info": {"polygons_id": [5, 9, 17], "fields": ["x", "y", "z"]},
    #"teams_info": {"teams_id": ["1"], "fields": ["team_members", "team_score"]}, 
    "servers_info": {"fields": ["adress", "workload"]}
    }

    # parsing
    test = data.Parser()
    
    print("response 1 = ", test.parse(request_1))
    print()

    print("response 2 = ", test.parse(request_2))
    print()
    
    pass

regTest()
pullTest()
requestTest()