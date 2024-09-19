from AVLTree import AVLTree
    
myTree = AVLTree() 
'''
# uncomment to build the tree from a list (only for empty tree)
nums = [42, 15, 88, 6, 27, 4] # right rotation
for node in nums:
    myTree.add(node)
'''
# Simulação 
# 0. construção a partir de uma lista usando o build()
# 1. rotação à direita             2. rotação à esquerda
# 3. rotação à esquerda + direita  4. rotação à direita + esquerda
TESTE = 1
if TESTE == 0:
    myTree.build([42, 15, 88, 6, 27, 4]) 
    print(myTree)
    myTree.treeview()

    print('Height: ', myTree.height())
    print('Iterating over tree:')
    for node in myTree:
        print(node,end= ' ')
    print()

    print('__Contains__', 88 in myTree )
elif TESTE == 1:
    myTree.add(42)
    print(myTree)
    myTree.add(15)
    print(myTree)
    myTree.add(88)
    print(myTree)
    myTree.add(6)
    myTree.add(27)
    myTree.add(4)
    print('Pre-Order traversal')
    myTree.traversal() 
    print('\nIn-Order traversal')
    myTree.traversal(AVLTree.inorder)
    print('\nPos-Order traversal')
    myTree.traversal(AVLTree.postorder)
    print(myTree)
    myTree.treeview()
    """
The constructed AVL Tree would be 
        15 
        /  \ 
      06   42 
    /     /  \ 
    04   27   88
    """

elif TESTE == 2:
    myTree.add(120)
    myTree.add(100)
    myTree.add(130)
    myTree.add(80)
    myTree.add(110)
    myTree.add(150)
    myTree.add(200)
    myTree.treeview()
    myTree.traversal()   
elif TESTE == 3:
    myTree.add(120)
    myTree.add(110)
    myTree.add(150)
    myTree.add(80)
    myTree.add(130)
    myTree.add(200)
    myTree.treeview()
    print('\nInserting 100')
    myTree.add(100) # nó que provoca o balanceamento
    myTree.treeview()
    myTree.traversal()  
 

print('Search 88 = ', myTree.search(88))
print(len(myTree))
# teste de remoção
key = 15
if TESTE == 1:
    print()
    print('\nRemovendo o nó', key)
    root = myTree.delete(key)
    print('Deleted root:', root)
    myTree.traversal()
    myTree.treeview()



