#find the pythagorean triplets that work together
import math
def finder(nums):
    #a set of every square is created
    sets = set([n*n for n in nums])

    for a in nums:
        for b in nums:
            #finds a^2 + b^2 is in the set
            if a * a + b * b in sets:
                print(a, " squared + ", b, " squared = ", math.sqrt(a * a + b * b))
                return True
    return False




list = [3, 5, 12, 5, 13]
print(finder(list))
