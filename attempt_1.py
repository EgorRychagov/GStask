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
    def pull(cls, nature, field, _id = "") -> dict:
        if nature not in cls.all_data:
            return {nature : "not registered"}        

        if _id == "":
            return cls.all_data[nature][field]
        
        if _id not in cls.all_data:    
            return {_id : "not registered"}
                
        return cls.all_data[nature][_id][field]
        

class Parser:
    pass
