#having valid parrenthesis/brackets/etc that match
class paren(object):
  def check(self, s):
#a map for what matches with what
    parens = {
      '[' : ']',
      '{' : '}',
      '(' : ')',
    }
    #parens inverted
    inverse = {v:k for k,v in parens.items()}

    stack = []

    for c in s:
        #if character in the map append to stack
      if c in parens:
        stack.append(c)
        #if character in the inverse
        #if len stack 0 or if the top character in stack not match with the inverse matching character then false
      elif c in inverse:
        if len(stack) == 0 or stack[-1] != inverse[c]:
          return False
        else:
            #if match
          stack.pop()
    return len(stack) == 0

print(paren().check('(){([])}'))


