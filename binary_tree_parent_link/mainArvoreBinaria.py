from BinaryTree import BinaryTree

tree = BinaryTree(30)
tree.addLeftChild(15)
tree.addRightChild(17)
tree.downRight()
tree.addLeftChild(70)
tree.reset()
tree.downRight()
tree.addLeftChild(5)
tree.addRightChild(52)
tree.downLeft()
tree.addRightChild(77)

print('Root:',tree.getRoot())
print('Cursor:',tree.getCursor())

tree.preorder()
print()
tree.inorder()
print()
tree.postorder()
input('...')
chave = 150
if( tree.search( chave )):
    print('\nChave',chave,'está na árvore')
else:
    print('\nChave',chave,'NÃO está na árvore')


print('Cursor:',tree.getCursor())
chave = 77
tree.preorderTraversal()
tree.deleteNode(chave)
tree.preorderTraversal()
print()
print()
chave = 70
tree.preorderTraversal()
print()
tree.deleteNode(chave)
tree.preorderTraversal()




