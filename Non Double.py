"""
find the one number in the array which is not a duplicate of any other number in the array
-we can do a linear time solution with a hashmap by iterating through the array once also linear space
- we can also xor the numbers and if there is a duplicate it turns into a 0 and the non duplicate will be left/space is constant
"""
class Double(object):
    #takes in the array/list
    def number(self, nums):
        #make hashmap
        map = {}

        for n in nums:
            #for everynumber input into hashmap and increment the value by 1
            #if the key is in the map and it sees it again it wont be 1 as the key
            map[n] = map.get(n, 0) + 1

        for key, value in map.items():
            #if the value of the key is one means there is only one and return it
            if value == 1:
                return key
        #xor method
    def number2(self, nums):
        nonDouble = 0
        for n in nums:
            #xor everynumber and if it sees number again it will be set to 0
            #the value that doesnt have a double will be stored cuz it wont be 0
            nonDouble ^= n
        return nonDouble

print(Double().number([4,4, 6, 7, 8, 7, 8]))
print(Double().number2([4, 4, 6, 7,  8, 7, 8]))