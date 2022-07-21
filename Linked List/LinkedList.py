class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
    def __init__(self, value):
       node = Node(value) # Creating new node
       self.head = node
       self.tail = node
       self.length = 1



    def print_list(self):
      if self.head is None:
        print('No items in list')
      else:
        ll = list()
        temp = self.head
        while(temp != None):
          ll.append(str(temp.value))
          temp = temp.next
        print('-'.join(ll))
        print('Head: ',  self.head.value)
        print('Tail: ', self.tail.value)
        print()
      


    def append(self, value):
      node = Node(value)

      if self.head == None and self.tail == None:
        self.head = node
        self.tail = node
        self.length = 1
      else:
        self.tail.next = node 
        self.tail = node  
        self.length += 1
    

    def pop(self):
      print('Pop called...')
      print()
      if self.head is None:
        print('No items are there in list')
      
      elif self.head.next is None:
        print('Only one item in the list')
        print('Removing the item...')
        self.head = None
        self.tail = None
        self.length = 0
        print('Item removed successfully!')
        print()

      else:
        print('Current List: ')
        self.print_list()
        temp = self.head
        while(temp.next != self.tail):
          temp = temp.next
        print('Item removed successfully: ', self.tail.value)   
        self.tail = temp 
        self.tail.next = None
        self.length -=1
        #print('List after pop: ', self.print_list())


    def prepend(self, value):
      node = Node(value)
      if self.head is None:
        print('There was no node present. Adding as first node')
        self.head = node
        self.tail = node
        self.length = 1
      else:
        node.next = self.head
        self.head = node
        self.length +=1


    def pop_first(self):
      print('Pop First called...')
      print()
      if self.head is None:
        print('No items are there in list')
      
      elif self.head.next is None:
        print('Only one item in the list')
        print('Removing the item...')
        self.head = None
        self.tail = None
        self.length = 0
        print('Item removed successfully!')
        print()

      else:
        print('Current List: ')
        self.print_list()
        print('Item getting popped: ', self.head.value)
        self.head = self.head.next
        print('Item popped...')
        self.length -=1
      
    

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

    def set(self, index, value):
      if index < 0:
        print('Please give a positive index')
      elif index > self.length -1 :
        print('Required index value greater than number of elements in list')
      else:
        temp = self.head
        for i in range(self.length):
          if i == index:
             temp.value = value
          else:
            temp = temp.next


    # For insert
        # 1.) If the index value is less than or equal to 0 we are prepending the new node.
        # 2.) If the index value is greater than max index we are appending the new node.
        # 3.) For index values anywhere in between we are inserting the new node at that index.
    def insert(self, index, value):
      node = Node(value)
      if index <= 0:
        self.prepend(value)
      elif index > self.length -1 :
        self.append(value)
      else:
        temp = self.head
        for i in range(self.length):
          if i == index - 1:
            node.next = temp.next
            temp.next = node
            self.length +=1
            break
          else:
            temp = temp.next

    # For remove
        # 1.) If the index value is less than 0 we are throwing error.
        # 2.) If the index value is greater than max index we are throwing error.
        # 3.) If the index value is 0 we are popping first.
        # 4.) If the index value is the last index of the list we are popping the last element.
        # 3.) For index values anywhere in between we are removing the element at that index.
    def remove(self, index):
      if index < 0:
        print('Error')
      elif index > self.length -1 :
        print('Error')      
      else:
        temp = self.head
        if index == 0:
          self.pop_first()
        elif index == self.length -1:
          self.pop()
        else:
          for i in range(self.length):
            if i == index - 1:
              temp.next = temp.next.next
              self.length -= 1
              break
            else:
              temp = temp.next

    def reverse(self):

      if self.length == 0:
        print('No item present in list')

      else:
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        for _ in range(self.length - 1):
          temp.next = before
          before = temp
          temp = after
          after = after.next
        temp.next = before
      

if __name__ == '__main__':
  linked_list = LinkedList(11)
  
  #linked_list.append(12)

  linked_list.print_list()
  linked_list.reverse()
  linked_list.print_list()
  print(linked_list.length)
 
  



