# problem 1
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    # problem 2
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

apollo = Villager("Apollo", "Eagle", "pah")

print("problem 1")
print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 


bones = Villager("Bones", "Dog", "yip yip")
print("problem 2")
print(bones.greet_player("Michelle"))

print("problem 3")
bones.catchphrase = "ruff it up"