class InfoStack:

    _all_data = {}  # {"which_id" : {"_id" : fields: dict} or {"servers_id": {fields: dict}} 
    
    @classmethod
    def getValue(cls): # "field1 = value, field2 = value ..."
        print("Fields: 'field = value, ...' ", end = "")
        fields_str: str = input()
        fields = {}
        fields_sep : list = fields_str.split(", ")

        for subfield in fields_sep:
            splitted: list = subfield.split(" = ")
            fields.update({splitted[0]: splitted[1]})

        return fields

    @classmethod
    def register(cls, fields: dict, **kwargs):
        'Defines an info type + sets fields to id'

        which_id = kwargs['which_id']
        _id: any = -1
        paramless: bool = False

        if '_id' in kwargs:
            _id = kwargs['_id']
        else:
            paramless = True

        if which_id not in cls._all_data:
            cls._all_data.update({which_id : {}})

        if not paramless:
            if _id not in cls._all_data[which_id]:
                cls._all_data[which_id].update({_id : fields})
                return
            
            for field in fields:
                cls._all_data[which_id][_id].update({field : fields[field]})
            return 
        
        for field in fields: # paramless case
            cls._all_data[which_id].update({field : fields[field]}) 
        return
    
        
    @classmethod
    def pull(cls, fields: list, **kwargs):
        'Returns a chapter with pulling fields {field: value}'

        which_id = kwargs['which_id']
        _id: any = -1
        paramless: bool = False

        if '_id' in kwargs:
            _id = kwargs['_id']
        else:
            paramless = True

        fields_buf = {} # buffer to contain pulling fields

        if which_id not in cls._all_data:
            return {which_id : "not registered"}
        
        if not paramless:
            if _id in cls._all_data[which_id]:
                for field in fields:
                    fields_buf[field] = cls._all_data[which_id][_id][field]
                return fields_buf
            else:
                return {which_id + " " + str(_id) : "not registered"}

        for field in fields: # paramless case
            fields_buf[field] = cls._all_data[which_id][field]
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
            "servers_info" : "fields",
            "extra_paramless_info" : "fields"
        }
        paramless = {
            "servers_info" : "servers_id",
            "extra_paramless_info" : "extra_id"
        }

        response = {} 
        subresponse = list()

        for info in request:
            if info not in info_to_name_id:
                return {"requested info": "incorrect"}
            
            id_name = info_to_name_id[info]

            if id_name not in request[info]:
               return {"requested id name": "incorrect"}

            if info not in paramless:
                for id_inst in request[info][id_name]:
                    subresponse.append(InfoStack.pull(request[info]["fields"], which_id = id_name, _id = id_inst))

                response[info] = subresponse.copy()
                subresponse.clear()
            else:
                response[info] = InfoStack.pull(request[info]["fields"], which_id = paramless[info])

        return response