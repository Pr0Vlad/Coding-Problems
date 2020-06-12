"""
people standing in a line(queue and you need to re arange)
basically an input format is [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
the first number is the height the second is how many people are infront of them that are taller or equal to them
OUTPUT for EXAMPLE [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
need to re arange in a way that fits the input so it matches the line
"""
#good approach is to order the taqllest people first and then put the shorter ones where they would fit cuz it wont really effect taller guys
class Answer:
    def ReArange(self, people):
        #sorts by decreasing height and increasing how many people infront that r taller
        people.sort(key = lambda x: (-x[0], x[1]))
        sol = []
        for n in people:
            sol.insert(n[1], n)
        return sol


run = Answer()
list = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(run.ReArange(list))