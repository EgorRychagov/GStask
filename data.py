# request = {
#     "players_info": { "players_id": ["_id"], "fields": ["name_player", "team_player", "score_player", "data_role"]},
#     "polygons_info": {"polygons_id": ["_id"], "fields":["x", "y", "z"]},
#     "teams_info": {"teams_id": ["_id"], "fields": ["all"]} ##### need to define fields
#     "server_info": {"servers_id": ["_id"], "fields": ["all"]}
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

    all_data = {}     # {"which_id" : {"_id" : fields}}
    
    @classmethod
    def register(cls, which_id, _id, fields: {}): # defines an info type + sets fields to id
        
        if which_id not in cls.all_data:
            cls.all_data.update({which_id : {}})
        cls.all_data[which_id][_id] = fields
        
    @classmethod
    def pull(cls, which_id, _id, fields: list ): # returns a chapter with pulling fields {field: value}

        fields_buf = {} # buffer to contain pulling fields

        if which_id not in cls.all_data:
            return {which_id : "not registered"}

        for field in fields:
            fields_buf[field] = cls.all_data[which_id][_id][field]

        return fields_buf

class parser:

    def __init__(self):
        pass
        
    def parse(self, request: dict):

        subresponse = list()

        # form the response
        which_id: str
        info_buf: {}
        fields: []

        info_to_which_id = {
            "players_info" : "players_id",
            "polygons_info" :"polygons_id",
            "teams_info" : "teams_id",
            "servers_info" : "servers_id"
        }

        response = {} # will be returned

        for info in request:
    
            which_id = info_to_which_id[info]
            
            for _id in request[info][which_id]:
                subresponse.append(info_stack.pull(which_id, _id, request[info]["fields"]))

            response[info] = subresponse.copy()
            subresponse.clear()

        return response