# problem 1
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        mutuals = []
        for friend in self.friends:
            if friend in new_contact.friends:
                mutuals.append(friend.name)
        return mutuals

# Example Usage
bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal))  # ['Raymond', 'Fauna']

ankha.friends = [marshal]
print(bob.get_mutuals(ankha))  # []


# problem 2
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

# Add code here to link the above nodes
kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

#Example Usage:
print_linked_list(kk_slider)