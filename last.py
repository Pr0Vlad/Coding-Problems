"""
you get a sorted list and need to find the first and last appearence of a certain number in the list and return the indices

example if input is 1, 3, 3, 5, 7, 8, 9, 9, 15
if asked for 9 the indicie range is 6-9

lets do it in sub-linear time
"""
#this is binary search to solve it
class Range:
    def GetRange(self, nums, target):
        start = self.binarySearch(nums, 0, len(nums) - 1, target, True)
        finish = self.binarySearch(nums, 0, len(nums) - 1, target, False)

        start2 = self.binaryiterativeSearch(nums, 0, len(nums) - 1, target, True)
        finish2 = self.binaryiterativeSearch(nums, 0, len(nums) - 1, target, False)
        print("recursive version solution: ", start, finish)
        print("iterative version solution: ", start2, finish2)

    #recursive solution
    def binarySearch(self, nums, low, high, target, findFirst):
        if high < low:
            return -1
        mid = low + (high - low) // 2
        if findFirst:
            if (mid == 0 or target > nums[mid-1]) and nums[mid] == target:
                return mid
            if target > nums[mid]:
                return self.binarySearch(nums, mid + 1, high, target, findFirst)
            else:
                return self.binarySearch(nums, low, mid - 1, target, findFirst)
        else:
            if (mid == len(nums) - 1 or target < nums[mid + 1]) and nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return self.binarySearch(nums, low, mid - 1, target, findFirst)
            else:
                return self.binarySearch(nums, mid + 1, high, target, findFirst)

#iterative version
    def binaryiterativeSearch(self, nums, low, high, target, findFirst):
        while True:
            if high < low:
                return -1
            mid = low + (high - low) // 2
            if findFirst:
                if (mid == 0 or target > nums[mid-1]) and nums[mid] == target:
                    return mid
                if target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid -1
            else:
                if (mid == len(nums) - 1 or target < nums[mid + 1]) and nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

nums = [1, 3, 3, 5, 7, 8, 9, 9, 15]
x = 9
sol = Range();
sol.GetRange(nums, x)