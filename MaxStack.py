#this is for adding a functionality for the stack which will return the maximum number

class Max(object):
    def __init__(self):
        self.stack = []
        self.maxs = []

    def push(self, val):
        self.stack.append(val);

        if self.maxs and self.maxs[-1] > val:
            self.maxs.append(self.maxs[-1])
        else:
            self.maxs.append(val)

    def pop(self):
        if self.maxs:
            self.maxs.pop()
        return self.stack.pop()

    def max(self):
        return self.maxs[-1]



runner = Max()

runner.push(2)
print("pushing 2")
print("current MAX: ", runner.max(), "\n")

runner.push(1)
print("pushing 1")
print("current MAX: ", runner.max(), "\n")

runner.push(5)
print("pushing 5")
print("current MAX: ", runner.max(), "\n")

runner.push(3)
print("pushing 3", )
print("current MAX: ", runner.max(), "\n")

runner.push(7)
print("pushing 7")
print("current MAX: ", runner.max(), "\n")

runner.push(10)
print("pushing 10")
print("current MAX: ", runner.max(), "\n")