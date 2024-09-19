from BinaryTree import BinaryTree

# tree = BinaryTree()
# tree.build([1,2,3,None,4,5,None])
# tree.treeview()
# exit()
'''
 _1_ 
/   \
2   3
 \ /
 4 5
'''
tree = BinaryTree(30)
# tree.createRoot(30)
tree.addLeftChild(15)
tree.addRightChild(17)
tree.downLeft()
tree.addLeftChild(70)
tree.reset()
tree.downRight()
tree.addLeftChild(5)
tree.addRightChild(52)
tree.downLeft()
tree.addRightChild(77)
print(f'Initial tree: root {tree.getRoot()}, cursor = {tree.getCursor()}')
tree.treeview()
print('\nPreorder traversal:')
tree.traversal() # default: preorder
print('Inorder traversal:')
tree.traversal(BinaryTree.inorder)
print('Postorder traversal:')
tree.traversal(BinaryTree.postorder)
print('__str__() result')
print(tree)
print('Height:',tree.height())

key = 150
if( tree.search( key )):
    print('\nKey',key,'is found')
else:
    print('\nKey',key,'is not found')

print('\nCursor is now in:',tree.getCursor())
key = 77
print('Deleting',key,'...')
tree.delete(key)
tree.traversal(BinaryTree.preorder)
print()
print('\nCursor is now in:',tree.getCursor())
key = 70
print('Deleting',key,'...')
tree.delete(key)
tree.traversal(BinaryTree.preorder)
print('\nCount:',len(tree))
print(tree)

print('Iterating over tree:')
for node in tree:
    print(node,end= ' ')

print('\n__contains__ test:')
key = 52
if key in tree:
    print('\tKey',key,'is in the tree')
tree.clear()
print(tree)




