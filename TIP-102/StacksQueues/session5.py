# problem 1

def is_valid_post_format(posts):
  sign_dict = {"[": "]", "{": "}", "(": ")"}
  stack = []

  for i in posts:
    if i in sign_dict:
      stack.append(i)
    else: 
      if not stack: 
        return False
      top = stack.pop()
      if sign_dict[top] != i: 
        return False

  return True
      
print("Problem 1")
print(is_valid_post_format("()")) # true
print(is_valid_post_format("()[]{}")) # true
print(is_valid_post_format("(]")) # false

# problem 2
def reverse_comments_queue(comments):
  return comments[::-1]

print("Problem 2")
print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

# problem 3
def is_symmetrical_title(title):
  title = title.lower()
  
  l, r = 0, len(title) - 1

  while l < r:
    if not title[l].isalnum():
      l += 1
      continue
    if not title[r].isalnum():
      r -= 1
      continue
    if title[l] != title[r]:
      return False
    l += 1
    r -= 1
  
  return True

print("Problem 3")
print(is_symmetrical_title("A Santa at NASA")) # true
print(is_symmetrical_title("Social Media")) # false
