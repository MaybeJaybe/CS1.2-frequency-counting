from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)

  def create_arr(self, size):
    array = []
    for i in range(size):
      array.append(LinkedList())
    return array

  def hash_func(self, key):
    index = 1
    for char in key:
      index = index * 17
    return index % self.size

  def insert(self, key, value):
    data = (key, value)
    arr_index = self.hash_func(key)
    linked_list = self.arr[arr_index]
    linked_list_index = linked_list.find(key)

    if linked_list_index == -1:
      linked_list.append(data)
    else:
      linked_list.update(key) 
 
  # Example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    for LinkedList in self.arr:
      LinkedList.print_nodes()