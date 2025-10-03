# Problem 1:Dot Product of 2 Sparse Vectors 

class SparseVector:
    def __init__(self, nums):
        self.nums = nums

    def dotProduct(self, vec):
        total = 0
        for i in range(len(self.nums)):
            total += self.nums[i] * vec.nums[i]
        return total


# Example
v1 = SparseVector([1, 0, 0, 2, 3])
v2 = SparseVector([0, 3, 0, 4, 0])
print(v1.dotProduct(v2))

# efficient storage
class SparseVector:
    def __init__(self, nums):
        # store only non-zero values with their indices
        self.data = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.data[i] = num

    def dotProduct(self, vec):
        result = 0
        # loop through smaller dictionary for efficiency
        if len(self.data) < len(vec.data):
            for i, val in self.data.items():
                if i in vec.data:
                    result += val * vec.data[i]
        else:
            for i, val in vec.data.items():
                if i in self.data:
                    result += val * self.data[i]
        return result
