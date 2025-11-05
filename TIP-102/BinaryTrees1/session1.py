# Problem 1: Grafting Apples

r"""

You are grafting different varieties of apple onto the same root tree can produce 
many different varieties of apples! Given the following TreeNode class, create the 
binary tree depicted below. The text representing each node should should be used 
as the value.

The root, or topmost node in the tree TreeNode("Trunk") has been provided for you.

             Trunk
          /         \
      Mcintosh   Granny Smith
      /     \       /     \
    Fuji   Opal   Crab   Gala
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# Create the tree structure
root = TreeNode("Trunk")
root.left = TreeNode("Mcintosh")
root.right = TreeNode("Granny Smith")

# Left subtree
root.left.left = TreeNode("Fuji")
root.left.right = TreeNode("Opal")

# Right subtree
root.right.left = TreeNode("Crab")
root.right.right = TreeNode("Gala")

# Helper function to print tree level-order (optional)
def print_tree(root):
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# Example Usage:
print(print_tree(root))

# Example Output:
# ['Trunk', 'Mcintosh', 'Granny Smith', 'Fuji', 'Opal', 'Crab', 'Gala']



# Problem 2: Calculating Yield

"""

You have a fruit tree represented as a binary tree with exactly three nodes: 
the root and its two children. Given the root of the tree, evaluate the amount 
of fruit your tree will yield this year. The tree has the following form:

- Leaf nodes have an integer value.
- The root has a string value of either "+", "-", "*", or "-".
- The yield of a the tree is calculated by applying the mathematical operation to 
  the two children.

Return the result of evaluating the root node.

Evaluate the time complexity of your function. Define your variables and provide 
a rationale for why you believe your solution has the stated time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    if not root.left and not root.right:
        return root.val

    left_val = calculate_yield(root.left)
    right_val = calculate_yield(root.right)

    if root.val == "+":
        return left_val + right_val
    elif root.val == "-":
        return left_val - right_val
    elif root.val == "*":
        return left_val * right_val
    elif root.val == "/":
        return left_val / right_val
    else:
        raise ValueError("Invalid operator")

# Example Usage:
r"""
    +
  /   \
 7     5
"""
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

print(calculate_yield(apple_tree))

# Example Output:
# 12



# Problem 3: Ivy Cutting

"""

You have a trailing ivy plant represented by a binary tree. You want to take 
a cutting to start a new plant using the rightmost vine in the plant. Given 
the root of the plant, return a list with the value of each node in the path 
from the root node to the rightmost leaf node. If there is no right child, 
return only the root node value 
(the rightmost path in this case is just the root node).

Evaluate the time complexity of your function. Define your variables and provide 
a rationale for why you believe your solution has the stated time complexity. 
Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def right_vine(root):
    path = []
    current = root
    
    # Traverse down the rightmost path
    while current:
        path.append(current.val)
        current = current.right

    return path

# Example Usage:
r"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

r"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1)) 
print(right_vine(ivy2))

# Example Output:
# ['Root', 'Node2', 'Leaf3']
# ['Root']



# Problem 4: Ivy Cutting II

"""
If you implemented right_vine() iteratively in the previous problem, 
implement it recursively. If you implemented it recursively, 
implement it iteratively.

Evaluate the time complexity of your function. Define your variables 
and provide a rationale for why you believe your solution has the stated 
time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    if not root:
        return []
    
    return [root.val] + right_vine(root.right)

# Example Usage:

r"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

r"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))
# Example Output:

['Root', 'Node2', 'Leaf3']
['Root']



# Problem 5: Count the Tree Leaves

"""
You've grown an oak tree from a tiny little acorn and it's finally sprouting leaves! 
Given the root of a binary tree representing your oak tree, count the number of leaf 
nodes in the tree. A leaf node is a node that does not have any children.

Evaluate the time complexity of your function. Define your variables 
and provide a rationale for why you believe your solution has the stated time complexity. 
Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

# Example Usage:

r"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

r"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


print(count_leaves(oak1))
print(count_leaves(oak2))

# Example Output:
# 3
# 1