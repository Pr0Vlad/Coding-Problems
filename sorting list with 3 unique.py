"""
given an array with three different numbers only and have to sort it and solve it
example [3, 3, 2, 1, 3, 2, 1]
is = [1, 1, 2, 2, 3, 3, 3]
sorting techniques will take longer than need it and can be done in a single pass using a hashmap

"""
def sort(nums):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
        # the [1] means only that is a unique number in this case we have 1-9 unique
    return ([1] * count.get(1, 0) + [2] * count.get(2, 0) + [3] * count.get(3, 0) + [4] * count.get(4, 0) + [5] * count.get(5, 0)
            + [6] * count.get(6, 0) + [7] * count.get(7, 0) + [8] * count.get(8, 0) + [9] * count.get(9, 0))

print (sort([5, 5, 6, 2, 2, 6, 2, 4, 4, 5, 7, 7]))