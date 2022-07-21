class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None    

class DoublyLinkedList:
  def __init__(self,value):
    node = Node(value)
    self.head = node
    self.tail = node
    self.length = 1
    
  def append(self, value):
    node = Node(value)
    if self.head is None:
      print('No node in list')
      print('Adding the first node')
      self.head = node
      self.tail = node
      self.length +=1
    
    else:
      self.tail.next = node
      node.prev = self.tail
      self.tail = node
      self.length +=1

  def print_list(self):
    if self.length == 0:
      print('No item in list')
    else:
      ll = list()
      temp = self.head
      while temp != None:
        ll.append(str(temp.value))
        temp = temp.next
      print('-'.join(ll))

  def pop(self):
    if self.length == 0:
      print('No items in list')
    elif self.length == 1:
      print('Only one node present in list')
      self.head = None
      self.tail = None
      self.length = 0
      print('Item')
    else:
      self.tail = self.tail.prev
      self.tail.next = None
      self.length -=1

  def prepend(self, value):
    if self.length == 0:
      self.append(value)
    else:
      node = Node(value)
      node.next = self.head
      self.head.prev = node
      self.head = node
      self.length +=1    
    
  def pop_first(self):
    if self.length == 0:
      print('No items in the list')
    elif self.length == 1:
      print('Only one node present in list')
      self.head = None
      self.tail = None
      self.length = 0
      print('Item')
    else:
      self.head = self.head.next
      self.head.prev = None
      self.length -= 1

  def get(self, index):
    if index < 0:
        print('Please give a positive index')
    elif index > self.length -1 :
        print('Required index value greater than number of elements in list')
    else:
      temp = self.head
      for i in range(self.length):
        if i == index:
          return temp.value
        else:
          temp = temp.next

if __name__ == '__main__':
  dll = DoublyLinkedList(11)
  dll.print_list()
  dll.append(12)
  dll.append(13)
  dll.append(14)
  dll.print_list()
  dll.pop_first()
  dll.print_list()
  print('Head:', dll.head.value)
  print('Tail:', dll.tail.value)
  print(dll.get(3))
  # dll.print_list()
  # dll.pop()
  # dll.print_list()      
  # print('Head:', dll.head.value)
  # print('Tail:', dll.tail.value)

