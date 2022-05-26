class SingleNode:
  def __init__(self, data):
    self.__data = data
    self.__next = None

  def get_data(self):
    return self.__data

  def get_next(self):
    return self.__next
    
  def set_next(self, node):
    self.__next = node