class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None
  
  def insert(self, value):
    node = Node(value)
    if self.root is None:
      self.root = node
      print('Inserted as root node')
      print(self.root.value)
      return

    else:
      temp = self.root
      while(temp != None):
          if node.value == temp.value:
            print('Node already present in the tree')
            return

          elif node.value < temp.value:
            if temp.left is None:
              temp.left = node
              print('Inserted {} successfully to left of {}'.format(node.value, temp.value))
              return
            else:
              temp = temp.left
          else:
            if temp.right is None:
              temp.right = node
              print('Inserted {} successfully to right of {}'.format(node.value, temp.value))
              return
            else:
              temp = temp.right

  def find(self, value):
      print('Finding {}...'.format(value))
      if self.root is None:
        print('The tree has no nodes')

      else:
        temp = self.root
        previous = self.root
        found = False

        while (temp !=None):
          if value < temp.value:
            previous = temp
            temp = temp.left
            if temp !=None:
              if temp.value == value:
                print('Found {} to the left of {}'.format(value, previous.value))
                found = True
                break
            else:
              print('Item not present in tree')
              return
          else:
            previous = temp
            temp = temp.right
            if temp !=None:
              if temp.value == value:
                print('Found {} to the right of {}'.format(value, previous.value))
                found = True
                break
            else:
              print('Item not present in tree')
              return
        if found:
          print('Item found!')
        else:
          print('Item not present in the tree')
      

if __name__ == '__main__':
  bst = BST()  
  bst.insert(100)
  bst.insert(50)
  bst.insert(60)
  bst.insert(70)
  bst.insert(150)
  bst.insert(110)
  bst.insert(30)
  bst.insert(20)
  bst.insert(40)

  print()
  bst.find(30)
  print()
  bst.find(60)
  print()
  bst.find(0)
  print()
  bst.find(20)