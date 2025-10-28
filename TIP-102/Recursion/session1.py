# PROBLEM 1
def count_suits_iterative(suits):
    count = 0
    for _ in suits:
        count += 1
    return count

def count_suits_recursive(suits):
    # Base case: if the list is empty, return 0
    if suits == []:
        return 0
    # Recursive case: 1 (for the first suit) + count of the rest
    return 1 + count_suits_recursive(suits[1:])

# Example usage
print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))


# PROBLEM 2
def sum_stones(stones):
    if not stones:
        return 0
    return stones[0] + sum_stones(stones[1:])

# Example usage
print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))
