class InfoStack:
    all_data = {}
# {
#   nature :    {
#                  _id  :       {
#                               field : value
#                               }
#               }
#   nature :    {
#                   field : value
#               }
# }

    responses = {}
    index = 0
    evoke = False
    
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
        
        if cls.evoke:
            for index in cls.responses:
                if nature in cls.responses[index]:
                    if _id in cls.responses[index][nature]:
                        cls.responses[index][nature][_id].update({field : value_getter()})
                        return
                    cls.responses[index][nature].update({field : value_getter()})

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
        

class Parser:
#   request = {
#           nature : {"_id" : [], "fields" : []}
#           nature : {"fields" : []}
#             }
#   response = {
#           nature : {"id" : {fields : values}}
#           nature : {fields : values}
#              }

    def __init__(self, request: dict):
        self.response = Parser.parse(request)
        InfoStack.evoke = True
        InfoStack.responses.update({InfoStack.index : self.response})
        InfoStack.index += 1

    def get_response(self):
        return self.response

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