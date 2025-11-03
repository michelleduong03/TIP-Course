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

# PROBLEM 4
def is_profitable(excursion_counts):
    n = len(excursion_counts)
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2  # potential x
        # find first index where excursion_counts[i] >= mid
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if excursion_counts[m] >= mid:
                r = m - 1
            else:
                l = m + 1
        count = n - l  # number of excursions with ≥ mid passengers

        if count == mid:
            return mid
        elif count > mid:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Example Usage
print(is_profitable([3, 5]))   # 2
print(is_profitable([0, 0]))   # -1

# PROBLEM 5
def find_shallowest_point(depths):
    # Base case: single element
    if len(depths) == 1:
        return depths[0]
    
    # Split the array
    mid = len(depths) // 2
    left_min = find_shallowest_point(depths[:mid])
    right_min = find_shallowest_point(depths[mid:])
    
    # Return the smaller of the two
    return left_min if left_min < right_min else right_min

# Example Usage
print(find_shallowest_point([5, 7, 2, 8, 3]))  # 2
print(find_shallowest_point([12, 15, 10, 21])) # 10

# PROBLEM 6
def find_treasure(matrix, treasure):
    if not matrix or not matrix[0]:
        return (-1, -1)
    
    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1  # start top-right corner
    
    while row < m and col >= 0:
        if matrix[row][col] == treasure:
            return (row, col)
        elif matrix[row][col] > treasure:
            col -= 1  # move left
        else:
            row += 1  # move down
            
    return (-1, -1)

# Example Usage
rooms = [
    [1, 4, 7, 11],
    [8, 9, 10, 20],
    [11, 12, 17, 30],
    [18, 21, 23, 40]
]

print(find_treasure(rooms, 17))  # (2, 2)
print(find_treasure(rooms, 5))   # (-1, -1)
