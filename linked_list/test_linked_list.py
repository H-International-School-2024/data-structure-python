from nodes import SingleNode

def size(node):
  if (node == None):
    return 0
  else :
    return 1 + size(node.get_next())

head = SingleNode(5)

second_node = SingleNode(6)
second_node.set_next(SingleNode(7))

head.set_next(second_node)

current_node = head
count = 0
while (current_node != None):
  count = count + 1
  current_node = current_node.get_next()

print(size(head))
print(count)

new_node = SingleNode(8)

