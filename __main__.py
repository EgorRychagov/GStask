import data

def regTest():
    # REAL TIME DATA PROCESSING
    print("REAL TIME PROCESSING")
    data.InfoStack.register(data.InfoStack.getValue(), which_id = "players_id", _id = "11")
    print("Real time registered = ", data.InfoStack.pull(["name_player", "team_player"], which_id = "players_id", _id = "11"), "\n")

    print("REG TEST:\n")
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

    for i in range(10):
        data.InfoStack.register(players_fields[i], which_id = "players_id", _id = str(i))

    # TEAMS 
    team_1_fields = {
        "team_members" : ["1", "2", "3", "4", "5"],
        "team_score" : 30
    }

    team_2_fields = {
        "team_members" : ["6", "7", "8", "9", "10"],
        "team_score" : 25
    }

    data.InfoStack.register(team_1_fields, which_id = "teams_id", _id = "team_1")
    data.InfoStack.register(team_2_fields, which_id = "teams_id", _id = "team_2")

    # POLYGONS 
    polygon_fields = []

    for i in range(20):
        polygon_fields.append({"x" : i, "y" : i+1, "z" : i+2})

    for i in range(20):
        data.InfoStack.register(polygon_fields[i], which_id = "polygons_id", _id = i)

    # SERVERS 
    server_fields = {
        "adress" : "Stockholm",
        "capacity" : 10,
        "workload" : 7
    }    

    data.InfoStack.register(server_fields, which_id = "servers_id")

    # EXTRA PARAMLESS INFO

    extra_fields = {
        "something" : "dskaod",
        "more fields" : "huwq"
    }

    data.InfoStack.register(extra_fields, which_id = "extra_id")

    print("Data was registered\n")

def pullTest():
    print("PULL TEST:\n")

    print("1) Existing data / all fields: \n")
    print("player = ", data.InfoStack.pull(["name_player", "score_player", "team_player", "data_role"], which_id = "players_id", _id = "3"))
    print("team = ", data.InfoStack.pull(["team_members", "team_score"], which_id = "teams_id", _id = "team_1"))
    print("polygon = ", data.InfoStack.pull(["x", "y"], which_id = "polygons_id", _id = 2))
    print("server = ", data.InfoStack.pull(["adress", "workload"], which_id = "servers_id"), "\n")

    print("2) Abscent data included\n")
    print(data.InfoStack.pull(["name_player", "team_player"], which_id = "players_id", _id = 5), "\n")  #id not registered


    print("3) Extra paramless info\n")
    print("extra_paramless_info = ", data.InfoStack.pull(["something"], which_id = "extra_id"), "\n")

def requestTest():
    print("REQUEST TEST:\n")
    print("1) All the data exists\n")

    test = data.Parser()

    request_1 = {
        "players_info": { "players_id": ["1", "7"], "fields": ["name_player", "team_player", "score_player", "data_role"]},
        "polygons_info": {"polygons_id": [5, 9, 17], "fields": ["x", "y", "z"]},
        "teams_info": {"teams_id": ["team_1"], "fields": ["team_members", "team_score"]}, 
        "servers_info": {"fields": ["adress", "capacity"]},
        "extra_paramless_info" : {"fields": ["something"]}
    }

    print("response 1 (with extra paramless info) = ", test.parse(request_1), "\n")
    print("2) Not registered data requested\n")
    
    request_2 = {
        "players_info": { "players_id": ["1", "-5"], "fields": ["name_player", "team_player", "score_player", "data_role"]},
        "polygons_info": {"polygons_id": [5, 9, 33], "fields": ["x", "y", "z"]}
    }

    print("response 2 = ", test.parse(request_2), "\n")
    print("3) Incorrect info in request\n")

    request_3 = {
        "polnaya": { "players_id": ["1", "7"], "fields": ["name_player", "team_player", "score_player", "data_role"]},
        "shnyaga": {"polygons_id": [5, 9, 17], "fields": ["x", "y", "z"]},
        "prosto": {"teams_id": ["team_1"], "fields": ["team_members", "team_score"]}, 
        "uzhas": {"fields": ["adress", "capacity"]}
    }

    print("response 2 = ", test.parse(request_3), "\n")
    print("4) Incorrect id name was requested:\n")

    request_4 = {
        "players_info": { "false id": ["1", "-5"], "fields": ["name_player", "team_player", "score_player", "data_role"]},
    }

    print("response 4 = ", test.parse(request_4), "\n")

regTest()
pullTest()
requestTest()