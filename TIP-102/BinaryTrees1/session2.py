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
    pass

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
    pass

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
    pass

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