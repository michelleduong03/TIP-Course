# Problem 1: Monstera Madness

"""
Given the root of a binary tree where each node represents the 
number of splits in a leaf of a Monstera plant, return the number 
of Monstera leaves 🍃 that have an odd number of splits.

Evaluate the time complexity of your function. Define your variables 
and provide a rationale for why you believe your solution has the 
stated time complexity.

Note: The term leaf in this problem refers to the plant leaf 🍃 
of a Monstera plant, not the type of node leaf nodes which are 
nodes with no children.
"""
from collections import deque 

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root
         
def count_odd_splits(root):
    if root is None:
        return 0
    
    count = 1 if root.val % 2 == 1 else 0
    
    count += count_odd_splits(root.left)
    count += count_odd_splits(root.right)
    
    return count

# Example Usage:
r"""
      2
     / \
    /   \
   3     5
  / \     \
 6   7     12
"""

# Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))
# Example Output:
# 3
# Example 1 Explanation: Three Monstera leaves (nodes) have 
# an odd number of fenestrations (3, 5, and 7).
# 0



# Problem 2: Flower Finding

"""
You are looking to buy a new flower plant for your garden. 
The nursery you visit stores its inventory in a binary search tree (BST) 
where each node represents a plant in the store. The plants are organized 
according to their names (vals) in alphabetical order in the BST.

Given the root of the binary search tree inventory and a target flower 
name, write a function find_flower() that returns True if the flower is 
present in the garden and False otherwise.

Evaluate the time complexity of your function. Define your variables and 
provide a rationale for why you believe your solution has the stated time 
complexity. Assume the input tree is balanced when calculating time complexity.
"""

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def find_flower(inventory, name):
    if inventory is None:
        return False
    if inventory.val == name:
        return True
    elif name < inventory.val:
        return find_flower(inventory.left, name)
    else:
        return find_flower(inventory.right, name)

# Example Usage:
r"""
         Rose
        /    \
      Lily   Tulip
     /  \       \
  Daisy  Lilac  Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 

# Example Output:
# True
# False



# Problem 3: Flower Finding II

"""
Consider the following function non_bst_find_flower() which accepts 
the root of a binary tree inventory and a flower name, and returns 
True if a flower (node) with name exists in the binary tree. Unlike 
the previous problem, this tree is not a binary search tree.

Compare your solution to find_flower() in Problem 2 to the following 
solution. Discuss with your group: How is the code different? Why?

What is the time complexity of non_bst_find_flower()? 

How does it compare to the time complexity of find_flower() in Problem 2?

How would the time complexity of find_flower() from Problem 2 
change if the tree inventory was not balanced?
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def non_bst_find_flower(root, name):
    if root is None:
        return False
    if root.val == name:
        return True
    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)

# Example Usage:
r"""
         Daisy
        /    \
      Lily   Tulip
     /  \       \
  Rose  Violet  Lilac
"""

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(non_bst_find_flower(garden, "Lilac"))  
print(non_bst_find_flower(garden, "Sunflower"))  

# Example Output:
# True
# False



# Problem 4: Adding a New Plant to the Collection

"""
You have just purchased a new houseplant and are excited to add it 
to your collection! Your collection is meticulously organized using a 
Binary Search Tree (BST) where each node in the tree represents a 
houseplant in your collection, and houseplants are organized alphabetically 
by name (val).

Given the root of your BST collection and a new houseplant name, 
insert a new node with value name into your collection. Return the 
root of your updated collection. If another plant with name already 
exists in the tree, add the new node in the existing node's right subtree.

Evaluate the time complexity of your function. Define your variables and 
provide a rationale for why you believe your solution has the stated time 
complexity. Assume the input tree is balanced when calculating time complexity.
"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


def add_plant(collection, name):
    if collection is None:
        return TreeNode(name)
    
    if name < collection.val:
        collection.left = add_plant(collection.left, name)
    else:  # name >= collection.val
        collection.right = add_plant(collection.right, name)
    
    return collection

# Example Usage:
r"""
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))
# Example Output:
# ['Money Tree', 'Fiddle Leaf Fig', 'Snake Plant', 'Aloe']
# Explanation: 
# Tree should have the following structure:
#            Money Tree
#         /              \
#  Fiddle Leaf Fig   Snake Plant
#    /
#  Aloe



# Problem 5: Sorting Plants by Rarity

"""
You are going to a plant swap where you can exchange cuttings of your 
plants for new plants from other plant enthusiasts. You want to bring
a mix of cuttings from both common and rare plants in your collection. 
You track your plant collection in a BST where each node has a key and 
a val. The val contains the plant name, and the key is an integer 
representing the plant's rarity. Plants are organized in the BST by their key.

To help choose which plants to bring, write a function sort_plants() 
which takes in the BST root collection and returns an array of plant 
nodes as tuples in the form (key, val) sorted from least to most rare. 
Sorted order can be achieved by performing an inorder traversal of the BST.
"""
class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key      # Plant rarity
        self.val = value      # Plant name
        self.left = left
        self.right = right


def sort_plants(collection):
    if collection is None:
        return []

    # Traverse left subtree
    left_sorted = sort_plants(collection.left)
    
    # Visit current node
    current_node = [(collection.key, collection.val)]
    
    # Traverse right subtree
    right_sorted = sort_plants(collection.right)
    
    # Combine results
    return left_sorted + current_node + right_sorted

# Example Usage:
r"""
         (3, "Monstera")
        /               \
   (1, "Pothos")     (5, "Witchcraft Orchid")
        \                 /
  (2, "Spider Plant")   (4, "Hoya Motoskei")
"""

# Using build_tree() function at the top of page
values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

print(sort_plants(collection))

# Example Output:
# [(1, 'Pothos'), (2, 'Spider Plant'), (3, 'Monstera'), (4, 'Hoya Motoskei'), (5, 'Witchcraft Orchid')]



# Problem 6: Finding a New Plant Within Budget

"""
You are looking for a new plant and have a max budget. The plant store 
that you are shopping at stores their inventory in a BST where each node 
has a key representing the price of the plant and value contains the plant's 
name. Plants are ordered by their prices. You want to find a plant that is 
close to but lower than your budget.

Given the root of the BST inventory and an integer budget, write a function 
pick_plant() that returns the plant with the highest price below budget. If no 
plant with a price strictly below budget exists, the function should return None.
"""
class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key      # Plant price
        self.val = val      # Plant name
        self.left = left
        self.right = right

def pick_plant(inventory, budget):
    result = None
    node = inventory
    
    while node:
        if node.key < budget:
            result = node.val  # candidate
            node = node.right  # try to find closer price below budget
        else:
            node = node.left  # price too high, go left
    
    return result

# Example Usage:
r"""
               (50, "Fiddle Leaf Fig")
             /                       \
    (25, "Monstera")           (70, "Snake Plant")
       /        \                   /         \
(15, "Aloe")  (40, "Pothos")  (60, "Fern")  (80, "ZZ Plant")
"""

# Using build_tree() function at the top of page
values = [(50, "Fiddle Leaf Fig"), (25, "Monstera"), (70, "Snake Plant"), (15, "Aloe"), 
            (40, "Pothos"), (60, "Fern"), (80, "ZZ Plant")]
inventory = build_tree(values)

print(pick_plant(inventory, 50)) 
print(pick_plant(inventory, 25)) 
print(pick_plant(inventory, 15)) 

# Example Output:

# Pothos
# Aloe
# None



# Problem 7: Remove Plant

"""
A plant in your houseplant collection has become infested with aphids, 
and unfortunately you need to throw it out. Given the root of a BST collection 
where each node represents a plant in your collection, and a plant name, 
remove the plant node with value name from the collection. Return the root 
of the modified collection. Plants are organized alphabetically in the tree by value.

If the node with name has two children in the tree, replace it with its inorder 
predecessor (rightmost node in its left subtree). You do not need to maintain a 
balanced tree.

Pseudocode has been provided for you.

Evaluate the time complexity of your function. Define your variables and provide a 
rationale for why you believe your solution has the stated time complexity. Assume 
the input tree is balanced when calculating time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def remove_plant(collection, name):
    if not collection:
        return None
    
    # Step 1: Traverse the tree to find the node
    if name < collection.val:
        collection.left = remove_plant(collection.left, name)
    elif name > collection.val:
        collection.right = remove_plant(collection.right, name)
    else:
        # Found the node to delete

        # Case 1: No children
        if not collection.left and not collection.right:
            return None

        # Case 2: One child
        if not collection.left:
            return collection.right
        if not collection.right:
            return collection.left

        # Case 3: Two children → replace with inorder predecessor
        predecessor = collection.left
        while predecessor.right:
            predecessor = predecessor.right

        # Replace value
        collection.val = predecessor.val

        # Delete the predecessor node from left subtree
        collection.left = remove_plant(collection.left, predecessor.val)
    
    return collection

# Example Usage:
r"""
              Money Tree
             /         \
           Hoya        Pilea
              \        /   \
             Ivy    Orchid  ZZ Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))

# Example Output:

# ['Money Tree', 'Hoya', 'Orchid', None, 'Ivy', None, 'ZZ Plant']

# Explanation:
# The resulting tree structure:
#              Money Tree
#             /         \
#           Hoya       Orchid
#               \          \
#               Ivy      ZZ Plant
