class Nature:
    def __init__(self, params: list):
        self.params = params 
        self.index = 0
        #self.params_amount = len(params)

    def _get_params(self):
        return self.params

class Entity(Nature):
    def __init__(self, nature: Nature, param_values: list): # fields [[values_param_1], [values_param_2], ...]
        self.nature = nature
        self.param_values = {} # {param : param_values : any}
        self.step = 0
        self.index = 0

        for param in nature._get_params():
            self.param_values.update({param : param_values[self.step]})
            self.step += 1
        step = 0
    
    def get_value(self, param):
        return self.param_values[param]
    
    def set_field(self, field, value):
        self.param_values["fields"][field] = value
    
class InfoStack:

    all_data: dict = {}

    @classmethod
    def register(cls, nature: Nature, entity: Entity):
        if entity.nature not in cls.all_data:
            cls.all_data.update({nature : {}})

        nature.index += 1
        entity.index = nature.index
        cls.all_data.update({nature : {entity.index : entity}})

    @classmethod
    def pull(cls, nature: Nature, entity: Entity) -> dict:
        if nature not in cls.all_data:
            return {"nature" : "not registered"}
        return cls.all_data[nature][entity.index].param_values

player = Nature(["id", "fields"])
player_1 = Entity(player, ["his_id", {"name_player" : "ckickname"}])

InfoStack.register(player, player_1)

print(InfoStack.pull(player, player_1), " -> just registered")
player_1.set_field("name_player", "ichiko")

print(InfoStack.pull(player, player_1), " -> field changed")

polygon = Nature(["id", "fields"])
polygon_1 = Entity(polygon, ["pol_id", {"x" : 0, "y" : 0, "z" : 0}])
InfoStack.register(polygon, polygon_1)
print(InfoStack.pull(polygon, polygon_1), " -> juat registered")

print(polygon_1.get_value("fields"))
polygon_1.set_field("x", 1)
InfoStack.register(polygon, polygon_1)
print(InfoStack.pull(polygon, polygon_1), " -> field changed")