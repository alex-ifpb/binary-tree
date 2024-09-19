from BinarySearchTree import BinarySearchTree

arv = BinarySearchTree()
# arv.build(['A', 'D', 'F', 'G', 'H', 'K', 'M', 'F'])
print('Adding nodes A, D, F, G, H, K, M, F...')
arv.add('A')
arv.add('D')
arv.add('F')
arv.add('G')
arv.add('H')
arv.add('K')
arv.add('M')
arv.add('F')
print('Len: ', len(arv))
print('Height: ', arv.height())
print('Printing using treeview()')
arv.treeview()

print('__Contains__', 'F' in arv )

print('Balance the tree...')
arv.balance()
print('OK')
print('Balance the tree...')
arv.treeview()

print('Iterating over tree:')
for node in arv:
    print(node,end= ' ')

print('\nCalling traversal() in preorder')
arv.traversal() # default: preorder
print('Print using __str__()')
print(arv)


print('\nSearch "H":', arv.search('H'))

print('\nRemove "G"')
arv.delete('G')
arv.traversal()
print('\nRemove "F"')
arv.delete('F')
arv.traversal()
print('\nRemove "H"')
arv.delete('H')
arv.traversal()
print('Root: ', arv.getRoot())
print('\nRemove "A"')
arv.delete('A')
arv.traversal()
print('Root: ', arv.getRoot())
print('\nRemove "D"')
arv.delete('D')
arv.traversal()
print('\nRemove "F"')
arv.delete('F')
arv.traversal()
print('Root: ', arv.getRoot())
print('\nRemove "M"')
arv.delete('M')
arv.traversal()
print('Root: ', arv.getRoot())
print('\nRemove "K"')
arv.delete('K')
arv.traversal()
print('Root: ', arv.getRoot())
print('Len: ', len(arv))








