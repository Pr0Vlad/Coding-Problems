#reversing a linked list
#a node has a value and a pointer to another node
#one way is to do it recursivley and another is iterative
class Node:
  def __init__(self, x):
    self.val = x
    self.next = None

  def __str__(self):
    pos = str(self.val)
    if self.next:
      pos += str(self.next)
    return pos

class Reverse:
    #iterative
    def reverse(self, head):
        prev = None
        cur = head
        #base cases
        while (cur != None):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    #recursive
    def reverse2(self, head):
        #base case if its last node pointing to nothing
        if head is None or head.next is None:
            return head
        #a new node becomes the node before it and repeats until nothing is before it
        current = self.reverse2(head.next)
        #sets the head to be the one after current node
        head.next.next = head
        #head.next is the current node
        head.next = None
        return current

node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)

run = Reverse();
print("iterative")
print(run.reverse(node))

node = Node(5)
node.next = Node(6)
node.next.next = Node(7)
node.next.next.next = Node(8)
print("recursive")
print(run.reverse2(node))