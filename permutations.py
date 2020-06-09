"""
given an array o integers print an array for every different possible permutation
"""
#using backtracking and swapping numbers in arrays
class perm:
    def sol(self, nums):
        out = []
        def sol2(start):
            if start == len(nums)-1:
                out.append(nums.copy())
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                sol2(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        sol2(0)
        return  out


runner = perm()
nums = [1, 2, 3]
print(runner.sol(nums))