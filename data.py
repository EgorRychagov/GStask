# request = {
#     "players_info": { "player_id": "_id", "fields": ["name_player", "team_player", "score_player", "data_role"]},
#     "polygons_info": {"polygon_id": "_id", "fields":["x", "y", "z"]},
#     "teams_info": {"team_id": "_id", "fields": ["all"]} ##### need to define fields
#     "server_info": {"server_id": "_id", "fields": ["all"]}
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
    _servers = {}

    @classmethod
    def register(self, which_id, _id, fields: {}): # defines an info type + sets fields to id

        if which_id == "player_id":
            self._players[_id] = fields
        elif which_id == "polygon_id":
            self._polygons[_id] = fields
        elif which_id == "team_id":
            self._teams[_id] = fields
        elif which_id == "server_id":
            self._servers[_id] = fields
        else:
            pass

    @classmethod
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
        
        elif which_id == "server_id":
            for field in fields:
                fields_buf[field] = self._servers[_id][field]
                return fields_buf

        else:
            pass

        fields_buf.clear();

class parser:

    def __init__(self):
        pass
        
    def parse(self, request: dict):

        response = {} # will be returned
        subresponse = list()

        # form the response
        _id: str
        info_buf: {}
        fields: []

        # run through subrequests
        for info in request:
    
            info_buf = request[info]
            fields = info_buf["fields"]

            if info == "players_info":
                _id = "player_id"
            elif info == "polygons_info":
                _id = "polygon_id"   
            elif info == "teams_info":
                _id = "team_id"
            elif info == "servers_info":
                _id = "server_id"
            else:
                pass
            

            #subresponse.append(info_stack.pull(_id, info_buf[_id], fields))
            #response[info] = subresponse

            response[info] = info_stack.pull(_id, info_buf[_id], fields)
            #subresponse.clear()
            #info_buf.clear()
            #fields.clear()
            
        return response