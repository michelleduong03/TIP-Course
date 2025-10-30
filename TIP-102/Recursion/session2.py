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