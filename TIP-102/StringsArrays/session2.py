# problem 1

'''

Write a function reverse_sentence() that takes in a string sentence and 
returns the sentence with the order of the words reversed. The sentence 
will contain only alphabetic characters and spaces to separate the words. 
If there is only one word in the sentence, the function should return the 
original string.

'''
def reverse_sentence(sentence):
    words = sentence.split()
    if len(words) == 1:       
        return sentence
    
    return " ".join(words[::-1])

sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)

# problem 2

def goldilocks_approved(nums):
    if len(nums) < 3: 
        return -1
    
    mn, mx = min(nums), max(nums)
    
    for num in nums:
        if num != mn and num != mx:
            return num
    return -1

nums = [3, 2, 1, 4]
goldilocks_approved(nums)

nums = [1, 2]
goldilocks_approved(nums)

nums = [2, 1, 3]
goldilocks_approved(nums)

# problem 3

def delete_minimum_elements(hunny_jar_sizes):
    res = []
    
    while hunny_jar_sizes:
        minimum = min(hunny_jar_sizes)
        res.append(minimum)
        hunny_jar_sizes.remove(minimum)
    
    print(res)

hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)

hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)

# problem 4

def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

num = 423
sum_of_digits(num)

num = 4
sum_of_digits(num)

# problem 5

def final_value_after_operations(operations):
    tigger = 1
    for op in operations:
        if op in ['bouncy', 'flouncy']:
            tigger += 1
        elif op in ['trouncy', 'pouncy']:
            tigger -= 1
    print(tigger)

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)

# problem 6

def is_acronym(words, s):
    if len(words) != len(s):
        return False
    
    for word, char in zip(words, s):
        if word[0] != char:
            return False
    return True

def is_acronym(words, s):
    if len(words) != len(s):
        return False

    for i in range(len(words)):
        if words[i][0] != s[i]:
            return False
    return True

words = ["christopher", "robin", "milne"]
s = "crm"
is_acronym(words, s)

# problem 7

def make_divisible_by_3(nums):
    total_ops = 0
    for num in nums:
        remainder = num % 3
        total_ops += min(remainder, 3 - remainder)
    return total_ops

nums = [1, 2, 3, 4]
make_divisible_by_3(nums)

nums = [3, 6, 9]
make_divisible_by_3(nums)

# problem 8

def exclusive_elemts(lst1, lst2):
    result = []
    for x in lst1:
        if x not in lst2:
            result.append(x)
    for x in lst2:
        if x not in lst1:
            result.append(x)
    return result

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
exclusive_elemts(lst1, lst2)

# problem 9

def merge_alternately(word1, word2):
    result = []
    i, j = 0, 0

    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1

    result.append(word1[i:])
    result.append(word2[j:])

    print("".join(result))

word1 = "wol"
word2 = "oze"
merge_alternately(word1, word2)

word1 = "hfa"
word2 = "eflump"
merge_alternately(word1, word2)

word1 = "eyre"
word2 = "eo"
merge_alternately(word1, word2)

# problem 10

def good_pairs(pile1, pile2, k):
    count = 0
    for i in range(len(pile1)):
        for j in range(len(pile2)):
            if pile2[j] * k != 0 and pile1[i] % (pile2[j] * k) == 0:
                count += 1
    print(count)

pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
good_pairs(pile1, pile2, k)

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
good_pairs(pile1, pile2, k)

###########
# ADVANCED
###########


# Problem 1

def transpose(matrix):
    # print([[row[i] for row in matrix] for i in range(len(matrix[0]))])
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)

    print(result)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix)

# Problem 2

def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]

        left += 1
        right -= 1

    return lst

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
reverse_list(lst)

# Problem 3

def remove_dupes(items):
    print(len(set(items)))

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
remove_dupes(items)

items = ["extract of malt", "haycorns", "honey", "thistle"]
remove_dupes(items)

# '''
# x can be a non negative integer
# build up a string
# based on x

# need a loop -> for loop going up to x

# empty result string
# building up result string

# append " batman!"
# return the output
# '''

# def nanana_batman(x):
#     res = ""

#     for i in range(x):
#         res += "na"

#     res += " batman!"
    
#     return res

# x = 6
# print(nanana_batman(x))


# '''

# binary array is an array with only 0s and 1s

# for loop -> conditional
# var to count 1s
# one that counts streak
# one that counts max streak
# if we have 1, update recent
# only when greater than curMax

# maxStreak = max(recentStreak, maxStreak)

# '''
# def maxConsecutivesOne():
#     pass

# nums = [1, 1, 0, 1, 1, 1]