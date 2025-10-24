# PROBLEM 1
"""
Problem 1: Wild Goose Chase

You're a detective and have been given an anonymous tip on your latest case, 
but something about it seems fishy - you suspect the clue might be a red herring 
meant to send you around in circles. Write a function is_circular() that accepts 
the head of a singly linked list clues and returns True if the tail of the linked 
list points at the head of the linked list. Otherwise, return False.

Evaluate the time and space complexity of your solution. Define your variables 
and provide a rationale for why you believe your solution has the stated time 
and space complexity.

Time: O(n)
Space: O(1)

"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
    if not clues:
          return False
    
    curr = clues

    while curr.next:
         if curr.next == clues:
              return True
         curr = curr.next

    return False

clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1))

# PROBLEM 2
"""
All the clues that lead us in circles are false evidence we need to purge! 
Given the head of a linked list evidence, clean up the evidence list by 
identifying any false clues. Write a function collect_false_evidence() that 
returns an array containing all values that are part of any cycle in evidence. 
Return the values in any order.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe 
your solution has the stated time and space complexity.

"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_false_evidence(evidence):
     visited = set()
     curr = evidence
     res = set()

     while curr:
          if curr in visited: # detected cycle
               start = curr
               while start not in res: # marked cycle
                  res.add(start)
                  start  = start.next
               break
          visited.add(curr)
          curr = curr.next

     return [node.value for node in res]

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))

# PROBLEM 3
