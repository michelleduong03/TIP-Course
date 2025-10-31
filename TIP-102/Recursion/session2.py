# PROBLEM 1
def find_cruise_length(cruise_lengths, vacation_length):
    low = 0
    high = len(cruise_lengths) - 1

    while low <= high:
        mid = (low + high) // 2
        if cruise_lengths[mid] == vacation_length:
            return True
        elif cruise_lengths[mid] < vacation_length:
            low = mid + 1
        else:
            high = mid - 1

    return False
 

print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))

# PROBLEM 2
# def find_cabin_index(cabins, preferred_deck):
#     def helper(low, high):
#         # Base case: insertion point
#         if low > high:
#             return low
        
#         mid = (low + high) // 2
        
#         if cabins[mid] == preferred_deck:
#             return mid
#         elif cabins[mid] < preferred_deck:
#             return helper(mid + 1, high)
#         else:
#             return helper(low, mid - 1)
    
#     return helper(0, len(cabins) - 1)
def find_cabin_index(cabins, preferred_deck):
    # Base case: if empty, return 0 (insert at start)
    if not cabins:
        return 0

    mid = len(cabins) // 2

    if cabins[mid] == preferred_deck:
        return mid
    elif cabins[mid] < preferred_deck:
        # Search right half, offset result by mid + 1
        return mid + 1 + find_cabin_index(cabins[mid + 1:], preferred_deck)
    else:
        # Search left half
        return find_cabin_index(cabins[:mid], preferred_deck)

print(find_cabin_index([1, 3, 5, 6], 5))  # 2
print(find_cabin_index([1, 3, 5, 6], 2))  # 1
print(find_cabin_index([1, 3, 5, 6], 7))  # 4

# PROBLEM 3
def count_checked_in_passengers(rooms):
    left, right = 0, len(rooms) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if rooms[mid] == 0:
            left = mid + 1
        else:
            right = mid - 1
            
    return len(rooms) - left

# Example usage
rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1))  # 4
print(count_checked_in_passengers(rooms2))  # 1
print(count_checked_in_passengers(rooms3))  # 0

#