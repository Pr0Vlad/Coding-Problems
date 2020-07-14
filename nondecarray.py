#if array is decreasing at any point can we fix it?
# like 4, 1, 2  decreases from 4-1
class solver(object):
    def possible(self, nums):
        index = -1
        for i in range(len(nums) -1 ):
            if nums[i] > nums[i+1]:
                #if more than two points going decreasing
                if index != -1:
                    return False
                index = i

        if index == -1:
            return True
        if index == 0:
            return True
        #can still adjust first and last point and make it work
        if index == len(nums) - 2:
            return True
        #here can also make it work with adjustments
        if nums[index] <= nums[index+2]:
            return True
        if nums[index - 1] <= nums[index + 1]:
            return True
        return False

runner = solver();
print(runner.possible([4, 1, 2]))

