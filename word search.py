#in a matrix of random characters the goal is to find if the word exists in the matrix left right or top bottom


#class for the matrix
class Node(object):
  def __init__(self, matrix):
    self.matrix = matrix


  def search(self, word):
    for i in range(len(self.matrix)):
      if self.row(i, word):
        return True
    for i in range(len(self.matrix[0])):
      if self.column(i, word):
        return True
    return False

#searches rows
  def row(self, index, word):
    for i in range(len(self.matrix[index])):
      if word[i] != self.matrix[index][i]:
        return False
    return True

#searches columns
  def column(self, index, word):
    for i in range(len(self.matrix)):
      if word[i] != self.matrix[i][index]:
        return False
    return True

matrix = [
    ['A', 'B', 'C', 'V'],
    ['P', 'L', 'A', 'C'],
    ['T', 'E', 'S', 'T'],
    ['D', 'J', 'T', 'G']]

print(Node(matrix).search('TEST'))
