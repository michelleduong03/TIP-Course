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
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def partition(suspect_ratings, threshold):
    greater = Node(0)  # dummy head for > threshold
    lesser = Node(0)   # dummy head for <= threshold
    g_tail, l_tail = greater, lesser
    current = suspect_ratings

    while current:
        if current.value > threshold:
            g_tail.next = current
            g_tail = g_tail.next
        else:
            l_tail.next = current
            l_tail = l_tail.next
        current = current.next

    g_tail.next = lesser.next  # join lists
    l_tail.next = None         # end the list
    return greater.next

suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(suspect_ratings, 3))

# PROBLEM 4
def merge_timelines(known_timeline, witness_timeline):
    dummy = Node(0)
    tail = dummy

    while known_timeline and witness_timeline:
        if known_timeline.value < witness_timeline.value:
            tail.next = known_timeline
            known_timeline = known_timeline.next
        else:
            tail.next = witness_timeline
            witness_timeline = witness_timeline.next
        tail = tail.next

    # Attach remaining nodes (if any)
    tail.next = known_timeline or witness_timeline

    return dummy.next

known_timeline = Node(1, Node(2, Node(4)))
witness_timeline = Node(1, Node(3, Node(4)))

print_linked_list(merge_timelines(known_timeline, witness_timeline))

# PROBLEM 5
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

def rotate_right(head, k):
    if not head or not head.next or k == 0:
        return head

    # Find the length and the tail
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Make it circular
    tail.next = head

    # Find new head after rotation
    k = k % length
    steps_to_new_head = length - k
    new_tail = head
    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail.next
    new_head = new_tail.next

    # Break the circle
    new_tail.next = None
    return new_head

# Example usage
evidence_list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
evidence_list2 = Node(0, Node(1, Node(2)))  # fixed typo: Noe -> Node

print_linked_list(rotate_right(evidence_list1, 2))
print_linked_list(rotate_right(evidence_list2, 4))
