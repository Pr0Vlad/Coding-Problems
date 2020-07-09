#say the array is size 4
#the new aray is also size 4 but say inidie 1 will be all indicies except one in original array that multiply against eachother
#force is too slow lets try linear time



class product:
  def multiply(self, nums):
      #set each value to one
    R = [1] * len(nums)
    result = 1
      #iterate back starting at smaller than last index and multiplying the index ahead
      #index two is 3 and multiplied by index 3 which is 4 is
      #24, 12, 4 is the outcome

    for i in range(len(nums) - 2, -1, -1):
      result *= nums[i+1]
      print(R)
      R[i] = result

    result = 1
      #when doing titeration from left side we get
      #1, 2, 6
    for i in range(1, len(nums)):

      result *= nums[i-1]
      print(R)
      R[i] *= result

    return R


print("final result", product().multiply([2, 3, 5, 1]))