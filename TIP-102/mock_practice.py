# PROBLEM 1
"""
Understand:


Match:


Plan:


Implement:


Review:


Evaluate:


"""

# PROBLEM 2
"""
Problem #2
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Input: haystack = "leetcode", needle = "leeto"
Output: -1

Understand:
haystack - string to search in
needle - string to search for
return index of the first occurence of needle in haystack
return -1 if not in haystack

Match:
sliding window approach
loop over indices

Plan:
1. loop over haystack
2. at each index i, check if the substring equals needle haystack[i:i+len(needle)]
3. if equals, return i
4. loop ends, no match return -1

Implement:


Review:


Evaluate:


"""

def problem_two(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1