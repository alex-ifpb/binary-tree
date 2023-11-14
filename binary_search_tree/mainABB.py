from BinarySearchTree import BinarySearchTree

arv = BinarySearchTree()
# arv.build(['A', 'D', 'F', 'G', 'H', 'K', 'M', 'F'])
print('Adding nodes...')
arv.add('A')
arv.add('D')
arv.add('F')
arv.add('G')
arv.add('H')
arv.add('K')
arv.add('M')
arv.add('F')
print('Len: ', len(arv))
arv.treeview()

print('Print in preorder traversal: traversal()')
arv.traversal() # default: preorder
print('Print using __str__()')
print(arv)

print('Iterating over tree:')
for node in arv:
    print(node,end= ' ')

print('\nSearch "H":', arv.search('H'))

print('\nRemove "G"')
arv.deleteNode('G')
arv.traversal()
print('\nRemove "F"')
arv.deleteNode('F')
arv.traversal()
print('\nRemove "H"')
arv.deleteNode('H')
arv.traversal()
print('Root: ', arv.getRoot())
print('\nRemove "A"')
arv.deleteNode('A')
arv.traversal()
print('Root: ', arv.getRoot())
print('\nRemove "D"')
arv.deleteNode('D')
arv.traversal()
print('\nRemove "F"')
arv.deleteNode('F')
arv.traversal()
print('Root: ', arv.getRoot())
print('\nRemove "M"')
arv.deleteNode('M')
arv.traversal()
print('Root: ', arv.getRoot())
print('\nRemove "K"')
arv.deleteNode('K')
arv.traversal()
print('Root: ', arv.getRoot())
print('Len: ', len(arv))








