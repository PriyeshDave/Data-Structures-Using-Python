class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self, value):
    node = Node(value)
    self.top = node
    self.length = 1
    
  def push(self, value):
    node = Node(value)
    if self.top is None:
      print('There is no item in stack')
      print('Pushing the first item...')
      self.top = node
      self.length = 1

    else:
      print('Pushing the node {}'.format(value))
      node.next = self.top
      self.top = node
      self.length +=1

  def print_stack(self):
    if self.top is None:
      print('There is no item present in stack')
    else:
      ll = list()
      temp = self.top
      while(temp != None):
        ll.append(str(temp.value))
        temp = temp.next
      print('-'.join(ll))

  def pop(self):
    if self.top is None:
      print('No items in the stack to be popped')
      self.length = 0
    else:
      print('Item getting popped: {}'.format(self.top.value))
      self.top = self.top.next
      self.length -= 1

if __name__ == '__main__':
  stack = Stack(11)
  stack.push(12)
  stack.push(13)
  stack.push(14)
  stack.print_stack()
  stack.pop()
  stack.print_stack()
  stack.pop()
  stack.pop()
  stack.pop()
  stack.print_stack()