#given an array of integers, return indicies of the two numbers so they add up to a specific targe.
# assume each input has one solution
# you may not use same element twice

# Given numbers =  2, 7, 11, 15
# target is 9
# 2 + 7 is 9 and the indicies are 0 and 1
# return 0, 1
#using a hashmap
#key is value of array
#value is the indicies
#look for the compliment in the table when reading each value inputed /o(2n) because looping twice through the array/once to input into hashmap and another time to find solution
#better to do the target number subtract the current number in the array and add to hashmap repeat until compliment is found in the hashmap
class TwoSum:
    def runner(self):
        #this is getting the array part
        nums = []
        print("input numbers to choose from and type any nondigit character when done")
        x = input()
        while x.isdigit():
            nums.append(int(x))
            x = input()
        print("enter target number")
        x = input()
        target = int(x)
    #this is the solution port
        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict:
                return [dict[target - num], i]
            dict[num] = i
        return "No Solution"


run = TwoSum()
sol = run.runner();
print(sol)