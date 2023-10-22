class InfoStack:
    all_data = {}
    requests = {}
    responses = {}
# {
#   nature :    {
#                  _id  :       {
#                               field : value_getter
#                               }
#               }
#   nature :    {
#                   field : value_getter
#               }
# }
    
    @classmethod
    def register(cls, nature, field, value_getter, _id = ""):
        if nature not in cls.all_data:
            cls.all_data.update({nature : {}})
        
        if _id == "":
            cls.all_data[nature].update({field : value_getter})

        cls.all_data[nature].update({_id : {field : value_getter}})
     
        # updating responses
#        response = {
#           nature : {"id" : {fields : values}}
#           nature : {fields : values}
#              }
        
        for name in cls.responses:
            if nature in cls.responses[name]:
                if _id in cls.responses[name][nature]:
                    cls.responses[name][nature][_id].update({field : value_getter()})
                    return
                cls.responses[name][nature].update({field : value_getter()})

    @classmethod
    def pull(cls, nature, field = "", _id = "") -> dict:
        if nature not in cls.all_data:
            return {nature : "not registered"}
        
        if _id == "":
            if field in cls.all_data[nature]:
                return {field : cls.all_data[nature][field]()}
            else: return {"field = " + str(field) : "not registered"}
        
        if _id not in cls.all_data[nature]:    
            return {"id = " + str(_id) : "not registered"}
        
        if field in cls.all_data[nature][_id]:    
            return {field : cls.all_data[nature][_id][field]()}
        
        return {"field = " + str(field) : "not registered"}
        
    @classmethod
    def request_reg(cls, name, request: dict):
        cls.requests.update({name : request})
        cls.responses.update({name : Parser.parse(request).copy()})

    @classmethod
    def request_pull(cls, name):
        if name not in cls.requests:
            return {"request = " + str(name) : "not registered"}
        return cls.requests[name]
        

class Parser:
#   request = {
#           nature : {"_id" : [], "fields" : []}
#           nature : {"fields" : []}
#             }
#   response = {
#           nature : {"id" : {fields : value_getters}}
#           nature : {fields : value_getters}
#              }
#   responses = {
#               request name : response with value_getters
#               }

    def __init__(cls):
        pass

    @classmethod
    def parse(cls, request: dict):
        response = {}
        subr_list = {}
        subresponse = {}

        for nature in request:
            if nature not in InfoStack.all_data:
                response.update({"nature = "+ str(nature) : "not registered"})
                continue
            
            response.update({nature : {}})

            if "_id" not in request[nature]:
                for field in request[nature]["fields"]:
                    subresponse.update(InfoStack.pull(nature, field))
                response[nature].update(subresponse.copy())
                subresponse.clear()
            else:
                for _id in request[nature]["_id"]:
                    if _id not in InfoStack.all_data[nature]:
                        subr_list.update({"id = " + str(_id) : "not registered"})
                        continue    

                    for field in request[nature]["fields"]:
                        subresponse.update(InfoStack.pull(nature, field, _id))
                    subr_list.update({_id : subresponse.copy()})
                    subresponse.clear()
                    
                response.update({nature : subr_list.copy()})
                subr_list.clear()

        return response