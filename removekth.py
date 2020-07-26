#removing the kth last element of a linked list for example 3rd would be third from last and then connect it
class Node:
#making nodes/node class
  def __init__(self, val, next):
    self.val = val
    self.next = next

#so we can print node as a string
  def __str__(self):
    value = self
    solution = ''
    while value:
      solution += str(value.val)
      value = value.next
    return solution

def removeK(node, k):
#using two pointes to find the element to remove
  p1, p2 = node, node
  for i in range(k):
    p2 = p2.next
  if not p2:
    return node.next

  prev = None
  while p2:
    prev = p1
    p2 = p2.next
    p1 = p1.next
  prev.next = p1.next
  return node

list = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
print(list)
head = removeK(list, 1)
print(list)
