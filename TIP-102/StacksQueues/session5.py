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
print(is_valid_post_format("(()())")) # true
print(is_valid_post_format("(){}[]")) # true


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

# problem 4
def engagement_boost(engagements):
  left, right = 0, len(engagements) - 1
  result = []

  while left <= right:
    if abs(engagements[left]) > abs(engagements[right]):
      result.append(engagements[left] ** 2)
      left += 1
    else:
      result.append(engagements[right] ** 2)
      right -= 1

  return result[::-1]

print("Problem 4")
print(engagement_boost([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
print(engagement_boost([-7, -3, 2, 3, 11]))  # [4, 9, 9, 49, 121]

# problem 5
def clean_post(post):
  stack = []

  for char in post:
    if stack and stack[-1] != char and stack[-1].lower() == char.lower():
      stack.pop() 
    else:
      stack.append(char)

  return "".join(stack)

print(clean_post("poOost")) # post
print(clean_post("abBAcC")) # 
print(clean_post("s")) # s

# problem 6
def edit_post(post):
    words = post.split()
    new_post = []
    for word in words:
        new_post.append(word[::-1])
    return " ".join(new_post)

print("Problem 6")
print(edit_post("Boost your engagement with these tips")) # tsooB ruoy tnemegegna htiw esehT spit
print(edit_post("Check out my latest vlog")) # kcehC tuo ym tseval golv

# probelm 7
def post_compare(draft1, draft2):
  def build(draft):
    stack = []
    for c in draft:
      if c == "#":
        if stack:
          stack.pop()
      else:
        stack.append(c)
    return "".join(stack)
    
  return build(draft1) == build(draft2)

print("Problem 7")
print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 