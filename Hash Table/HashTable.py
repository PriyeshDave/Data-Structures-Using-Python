class HashTable:
  def __init__(self, table_length = 6):
    self.table = [None] * table_length
    print('Hash Table created !')
    print()

  def create_hash_value(self, key):
    hash_value = 0
    for i in key:
      hash_value = (hash_value + ord(i)) % len(self.table)
    #print('Hash value created!')
    #print('{} : {}'.format(key, hash_value))
    #print()
    return hash_value
  
  def print_table(self):
    for i, val in enumerate(self.table):
      print('{} : {}'.format(i, val))
      print()


  def set_item(self, key, value):
    hash_index = self.create_hash_value(key)
    print('Setting item [{}, {}] to table...'.format(key, value))
    if self.table[hash_index] is None:
      self.table[hash_index] = []
    self.table[hash_index].append([key, value])
    print('Item set!')
    print()
  
  def get_item(self, key):
    hash_index = self.create_hash_value(key)
    print('Getting value of {}...'.format(key))
    found = False

    if self.table[hash_index] is None:
      print('Item not present')
    else:
      for item in self.table[hash_index]:
        if item[0] == key:
          found = True
          break
      if found:
        print('Item found!')
        print('{} : {}'.format(key, item[1]))
        print()
      else:
        print('Item not present in the table!')
        print()

  def get_keys(self):
    print('Getting the keys from table...')
    all_keys = []
    for table_index in range(len(self.table)):
      if self.table[table_index] is None:
        continue
      if len(self.table[table_index]) != 0:
        for item in self.table[table_index]:
          all_keys.append(item[0])
    print('The keys are:')
    print(all_keys)
    print()        
      
if __name__ == '__main__':
  ht = HashTable()
  ht.set_item('Priyesh', 1)
  ht.set_item('Dave', 2)
  ht.set_item('Priyeshh', 3)

  ht.print_table()
  ht.get_item('Priyesh')
  ht.get_item('Dave')
  ht.get_item('Priyeshh')
  ht.get_item('Hello')
  ht.get_keys()