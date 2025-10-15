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
    
    # problem 4
    def set_catchphrase(self, new_catchphrase):
        # Check that the catchphrase is alphabetic or whitespace and less than 20 characters
        if len(new_catchphrase) < 20 and all(c.isalpha() or c.isspace() for c in new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase updated!")
        else:
            print("Invalid catchphrase")

    # Problem 5: Add Furniture
    def add_item(self, item_name):
        valid_items = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in valid_items:
            self.furniture.append(item_name)

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

