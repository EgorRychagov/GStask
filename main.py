# request = {
#     "players_info": { "param": "all", "fields": ["name_player", "team_player", "score_player", "data_role", "id"]},
#     "polygon_info": {"param":1, "fields":["position"]},
#     "team_info": {"param": "all", "fields": ["all"]}
# }
    
# response = {
#     "players_info": 
#     [
#         {
#             "name_player": "clickname",
#             "team_player": "team1",
#             "score_player": 100,
#             "data_role":{
#                 "name_role": "global_role"
#             },
#             "id": "1"
#         },
#         {
#             "name_player": "verony",
#             "team_player": "team2",
#             "score_player": 50,
#             "data_role":{
#                 "name_role": "global_role"
#             },
#             "id": "2"
#         }
#     ],

#     "teams_info":
#     [
#         {
#             "name_team": "team1",
#             "id_players":[]
#         },
#         {
#             "name_team": "team2",
#             "id_players":[]
#         }
#     ],

#     "polygon_info": 
#     [
#         {"position": [1, 1, 1]}
#     ]    
# }


class info_stack:
    
    state: str = ""

    info = {}

    def get_data(self):
        return self.state

    def register(self, data_type, get_data):
        self.info[data_type] = get_data

    def pull_one(self, what_to_pull):
        return self.info[what_to_pull]

class parser:
    data = info_stack

    players_info = {}
    polygons_info = {}
    teams_info = {}

    player_fields = []
    polygon_fields = []
    team_fields = []

    def __init__(self, request: dict):
        self.players_info = request["players_info"]
        self.polygons_info = request["polygons_info"]
        self.teams_info = request["teams_info"]

        self.player_fields: [] = self.players_info["fields"]
        self.polygon_fields: [] = self.polygon_fields["fields"]
        self.team_fields: [] = self.team_fields["fields"]

    response = {}

    def parse(self):
        self.response["players_info"] = []
        self.response["teams_info"] = []
        self.response["polygons_info"] = []

        buf_addon = {}

        for field in self.player_fields:
            buf_addon[field] = self.data.pull_one(field)

        self.response["players_info"].append(buf_addon)
        buf_addon.clear()

        for field in self.team_fields:
            buf_addon[field] = self.data.pull_one(field)

        self.response["teams_info"].append(buf_addon)
        buf_addon.clear()

        for field in self.polygon_fields:
            buf_addon[field] = self.data.pull_one(field)

        self.response["polygons_info"].append(buf_addon)
        buf_addon.clear()

        return self.response
