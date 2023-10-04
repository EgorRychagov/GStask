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

class InfoStack:

    _all_data = {}  # {"which_id" : {"_id" : fields: dict} or {"servers_id": {fields: dict}}
        
    @classmethod
    def register(cls, fields: dict, **kwargs):
        'Defines an info type + sets fields to id'

        which_id = kwargs['which_id']
        _id: any = -1
        if '_id' in kwargs:
            _id = kwargs['_id']

        if which_id not in cls._all_data:
            cls._all_data.update({which_id : {}})
        
        if which_id == "servers_id":
            for field in fields:
                cls._all_data[which_id].update({field : fields[field]}) 
            return
        
        if _id not in cls._all_data[which_id]:
            cls._all_data[which_id].update({_id : fields})
            return
        
        for field in fields:
            cls._all_data[which_id][_id].update({field : fields[field]})
        return 
        
    @classmethod
    def pull(cls, fields: list, **kwargs):
        'Returns a chapter with pulling fields {field: value}'

        which_id = kwargs['which_id']
        _id: any = -1
        if '_id' in kwargs:
            _id = kwargs['_id']

        fields_buf = {} # buffer to contain pulling fields

        if which_id not in cls._all_data:
            return {which_id : "not registered"}
        
        if which_id == "servers_id":
            for field in fields:
                fields_buf[field] = cls._all_data[which_id][field]
            return fields_buf

        if _id in cls._all_data[which_id]:
            for field in fields:
                fields_buf[field] = cls._all_data[which_id][_id][field]
        else:
            return {which_id + " " + str(_id) : "not registered"}

        return fields_buf

class Parser:

    def __init__(self):
        pass
        
    def parse(self, request: dict):

        # form the response
        id_name: str
        info_buf: {}
        fields: []

        info_to_name_id = {
            "players_info" : "players_id",
            "polygons_info" :"polygons_id",
            "teams_info" : "teams_id",
            "servers_info" : "servers_id"
        }

        response = {} 
        subresponse = list()

        for info in request:
            
            id_name = info_to_name_id[info]
    
            if info != "servers_info":
                
                for id_inst in request[info][id_name]:
                    subresponse.append(InfoStack.pull(request[info]["fields"], which_id = id_name, _id = id_inst))

                response[info] = subresponse.copy()
                subresponse.clear()
            else:
                response[info] = InfoStack.pull(request[info]["fields"], which_id = id_name)

        return response