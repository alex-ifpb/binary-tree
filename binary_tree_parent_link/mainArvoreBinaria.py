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
print('Altura:',tree.height())
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

tree.treeview()

print('Arvore vazia: ', tree.isEmpty())
print('Altura:',tree.height())
print('Iterador:')
for e in tree:
    print(e,  end=' ')

print('\nRoot:',tree.getRoot())
print('Cursor:',tree.getCursor())
print('__contains__:', 521 in tree)

tree.traversal(BinaryTree.preorder)
print()
tree.traversal(BinaryTree.inorder)
print()
tree.traversal(BinaryTree.postorder)
input('...')
chave = 150
if( tree.search( chave )):
    print('\nChave',chave,'está na árvore')
else:
    print('\nChave',chave,'NÃO está na árvore')


print('Cursor:',tree.getCursor())
chave = 77
tree.traversal(BinaryTree.preorder)
tree.delete(chave)
tree.traversal(BinaryTree.preorder)
print()
print()
chave = 70
tree.traversal(BinaryTree.preorder)
print()
tree.delete(chave)
tree.traversal(BinaryTree.preorder)

tree.clear()
tree.treeview()



