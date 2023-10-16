import data_shell

class Player:
    def __init__(self, name, score, team):
        self.name = name
        self.score = score
        self.team = team
        
    def get_name(self):
        return self.name
    
    def get_score(self):
        return self.score
    
    def get_team(self):
        return self.team
    
class Server:
    def __init__(self, capacity, adress):
        self.adress = adress
        self.capacity = capacity
    
    def get_adress(self):
        return self.adress
    
    def get_capacity(self):
        return self.capacity
    
print("USAGE EXAMPLE:")

player_1 = Player("clickname", 13, "VP")
data_shell.InfoStack.register("player", "name", player_1.get_name, "1")

print("\t1) Player's name was registered and pulled by _id:", data_shell.InfoStack.pull("player", "name", "1"))

player_1.name = "no clickname anymore"
data_shell.InfoStack.register("player", "name", player_1.get_name, "1")
print("\t2) Player's name was changed and pulled by _id:", data_shell.InfoStack.pull("player", "name", "1"))

server = Server(10,"Stockholm")
data_shell.InfoStack.register("server", "adress", server.get_adress)

print("\t3) Server was registered with no _id:", data_shell.InfoStack.pull("server", "adress"))

server.capacity = 10
data_shell.InfoStack.register("server", "capacity", server.get_capacity)

print("\t4) Server's capacity was added in data:", data_shell.InfoStack.pull("server", "capacity",))
print("\nEXEPTIONS:")

print("\t1) Pulling unregistered nature:", data_shell.InfoStack.pull("team"))
print("\t2) Pulling player's name by unregistered _id", data_shell.InfoStack.pull("player", "name", "2"))
print("\t3) Pulling unregistered field of player by _id:", data_shell.InfoStack.pull("player", "team", "1"))
print("\t4) Pulling server's unregistered field with no _id:", data_shell.InfoStack.pull("server", "workload"))

print("\nREQUEST -> RESPONSE:")

request = {
    "player": {"_id" : ["1", "2"], "fields" : ["name", "team"]},
    "server" : {"fields" : ["capacity", "adress"]}
           }
parser = data_shell.Parser

print("\tRequest = ", request)
print("\tResponse = ", parser.parse(request))