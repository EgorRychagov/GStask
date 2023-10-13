class InfoStack:
    all_data = {}

    # {
    #   nature :    {
    #                  _id  :       {
    #                               field : value
    #                               }
    #               }
    # }

    @classmethod
    def register(cls, nature, field, value_getter, _id = ""):
        if nature not in cls.all_data:
            cls.all_data.update({nature : {}})

        if _id == "":
            cls.all_data[nature].update({field : value_getter})

        cls.all_data[nature].update({_id : {field : value_getter}})
        print(cls.all_data)
        
    @classmethod
    def pull(cls, nature, field = "", _id = "") -> dict:
        if nature not in cls.all_data:
            return {nature : "not registered"}
        
        if _id == "":
            if field in cls.all_data[nature]:
                return {field : cls.all_data[nature][field]()}
            else: return {field : "not registered"}
        
        if _id not in cls.all_data:    
            return {_id : "not registered"}
        
        if field in cls.all_data[nature][_id]:    
            return {field : cls.all_data[nature][_id][field]()}
        
        return {field : "not registered"}
        

class Parser:
    def parse(request: dict):
        response = {}
        subr_list = {}
        subresponse = {}

        for nature in request:
            if nature not in InfoStack.all_data:
                response.update({nature : "not registered"})
                continue
            
            response.update({nature : {}})

            if "_id" not in request[nature]:
                for field in request[nature]:
                    subresponse.update(InfoStack.pull(nature, field))
                response[nature].update(subresponse.copy())
                subresponse.clear()

            for _id in request[nature]:
                if _id not in InfoStack.all_data[nature]:
                    subr_list.update({_id : "not registered"})

                for field in request[nature][_id]:
                    subresponse.update(InfoStack.pull(nature, field, _id))
                subr_list.update({_id : subresponse.copy()})
                subresponse.clear()
                
            response.update({nature : subr_list.copy()})
            subr_list.clear()

        return response