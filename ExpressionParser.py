#make a calculator that can use pemdas to solve expressions
#this is a shorr version given the expression entered has no syntax errors
import re

def calculate(expression):
    index = 0
    char = []
    result = 0;
    array = []

#tokenizing the input into symbols
    for i in expression:
        i = i.strip()
        if i != "":
            newEx = re.match('\\S', i).group(0)
            char.append(newEx)

    parser(char, index, result, array)


    return char;

#constructed LL1 parser for grammer to do classic pemdas math
# E -> T | E'
# E' -> + T E' | -T E' | Epsilon
# T -> F T'
# T' -> * F T' | /F T' | Eplison
# F -> ( E ) | integer
class parser:

    def __init__(self, tokens = [], index = int, result = int, array = []):
        self.index = index
        self.tokens = tokens
        self.array = array
        self.e()
        print("left array", self.array)




    def getIndex(self):
        return self.index
    def addIndex(self):
        if self.index < len(self.tokens)-1:
            self.index += 1


    def e(self):

        #can go to T or can go to E'
        #checks if its a paren or a digit 1 token lookahead here
        self.t()
        self.ePrime()
        return

    def ePrime(self):
        if (self.tokens[self.index] == '+' or self.tokens[self.index] == '-'):
            print(self.tokens[self.index])
            self.array.append(self.tokens[self.index])
            self.addIndex()
            self.t()
            self.ePrime()
            return
        else:
            return

    def t(self):
        self.final()
        self.tPrime()
        return

    def tPrime(self):
        if (self.tokens[self.index] == '*' or self.tokens[self.index] == '/'):
            print(self.tokens[self.index])
            self.array.append(self.tokens[self.index])
            self.addIndex()
            self.final()
            self.tPrime()
            return
        else:
            return

    def final(self):
        if (self.tokens[self.index] == '('):
            self.array.append(self.tokens[self.index])
            print(self.tokens[self.index])
            self.addIndex()
            self.e()


            #after coming back from E
            if (self.tokens[self.index] == ')'):
                self.array.append(self.tokens[self.index])
                print(self.tokens[self.index])
                self.addIndex()

                return
        #checking for integer int
        elif  (self.tokens[self.index].isdigit()):
            print(self.tokens[self.index])
            self.array.append(self.tokens[self.index])
            self.addIndex()
            return
        else:
            return False

#print(calculate(' ( 7 - 2 ) '))
print(calculate(' - ( 5 * ( 7 - 2 ) ) '))