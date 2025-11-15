# Problem 1: Balanced Baked Goods Display

"""
Given the root of a binary tree display representing the baked goods 
on display at your store, return True if the tree is balanced and False otherwise.

A balanced display is a binary tree in which the difference in the height 
of the two subtrees of every node never exceeds one.

Evaluate the time complexity of your function. Define your variables and 
provide a rationale for why you believe your solution has the stated time complexity.
"""
from collections import deque
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


def is_balanced(display):
    def height(node):
        if not node:
            return 0

        left = height(node.left)
        right = height(node.right)

        # If either subtree already unbalanced, bubble up immediately
        if left == -1 or right == -1:
            return -1

        # If difference > 1 → unbalanced
        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    return height(display) != -1


# Example Usage:

r"""
      🎂
     /  \
   🥮   🍩
       /  \  
     🥖    🧁

"""
# Using build_tree() function included at top of page
baked_goods = ["🎂", "🥮", "🍩", None, None, "🥖", "🧁"] 
display1 = build_tree(baked_goods)

r"""
          🥖
         /  \
       🧁    🧁
       /       \  
      🍪       🍪
     /           \
    🥐           🥐  

"""
baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)


print(is_balanced(display1)) 
print(is_balanced(display2))  

# Example Output:

# True
# False



# Problem 2: Sum of Cookies Sold Each Day

"""
Your bakery stores each customer order in a binary tree, where each node 
represents a different customer's order and each node value represents the 
number of cookies ordered. Each level of the tree represents the orders for 
a given day.

Given the root of a binary tree orders, return a list of the sums of all 
cookies ordered in each day (level) of the tree.

Evaluate the time complexity of your solution. Define your variables and give 
a rationale as to why you believe your solution has the stated time complexity.
"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_each_days_orders(orders):
    if not orders:
        return []

    result = []
    queue = deque([orders])

    while queue:
        level_sum = 0
        size = len(queue)

        for _ in range(size):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_sum)

    return result


# Example Usage:

r"""
      4
     / \
    2   6
   / \  
  1   3
"""

# Using build_tree() function included at top of page
order_sizes = [4, 2, 6, 1, 3]
orders = build_tree(order_sizes)

print(sum_each_days_orders(orders))
# Example Output:

# [4, 8, 4]



class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sweet_difference(chocolates):
    pass