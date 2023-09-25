# request = {
#     "players_info": { "player_id": "_id", "fields": ["name_player", "team_player", "score_player", "data_role"]},
#     "polygons_info": {"polygon_id": "_id", "fields":["x", "y", "z"]},
#     "teams_info": {"team_id": "_id", "fields": ["all"]} ##### need to define fields
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
#         },# separate request to subrequests
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

    # {"id": {field:value}}
    _players = {}
    _polygons = {}
    _teams = {}

    @classmethod
    def register(self, which_id, _id, fields: {}): # defines an info type + sets fields to id

        if which_id == "player_id":
            self._players[_id] = fields
        elif which_id == "polygon_id":
            self._polygons[_id] = fields
        elif which_id == "team_id":
            self._teams[_id] = fields
        else:
            pass

    @staticmethod
    def pull(self, which_id, _id, fields: list ): # returns a chapter with pulling fields {field: value}

        fields_buf = {} # buffer to contain pulling fields

        if which_id == "player_id":
            for field in fields:
                fields_buf[field] = self._players[_id][field]
            return fields_buf 

        elif which_id == "polygon_id":
            for field in fields:
                fields_buf[field] = self._polygons[_id][field]
            return fields_buf 

        elif which_id == "team_id":
            for field in fields:
                fields_buf[field] = self._teams[_id][field]
            return fields_buf 
        
        else:
            pass

        fields_buf.clear();

class parser:

    # subrequests 
    players_info = {}
    polygons_info = {}
    teams_info = {}

    # fields
    player_fields = []
    polygon_fields = []
    team_fields = []

    def __init__(self):
        pass
        
    def parse(self, request: dict):

        response = {} # will be returned
        
        # form the response
        ## check existing subrequests
        if "players_info" in request:
            self.players_info = request["players_info"]
            self.player_fields = self.players_info["fields"]

            response_buf = list()
            # appending chapter {field: value} for single player in a list
            response_buf.append(info_stack.pull("player_id", self.players_info["player_id"], self.player_fields)) # list of single chapter for now
            response["players_info"] = response_buf

        elif "polygons_info" in request:
            self.polygons_info = request["polygons_info"]
            self.polygon_fields = self.polygons_info["fields"]

            response_buf = list()
            response_buf.append(info_stack.pull("polygon_id", self.polygons_info["polygon_id"], self.polygon_fields)) # single chapter in a list
            response["polygon_info"] = response_buf
        
        elif "teams_info" in request:    
           self.teams_info = request["teams_info"]
           self.team_fields = self.teams_info["fields"]

           response_buf = list()
           response_buf.append(info_stack.pull("team_id", self.teams_info["team_id"], self.polygon_fields)) # single chapter in a list
           response["teams_info"] = response_buf
        else:
            pass

        return self.response