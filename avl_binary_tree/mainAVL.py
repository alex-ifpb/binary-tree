from AVLTree import AVLTree
    
myTree = AVLTree() 
'''
# uncomment to build the tree from a list (only for empty tree)
nums = [42, 15, 88, 6, 27, 4] # right rotation
for node in nums:
    myTree.insert(node)
'''
# Simulação 
# 0. construção a partir de uma lista usando o build()
# 1. rotação à direita             2. rotação à esquerda
# 3. rotação à esquerda + direita  4. rotação à direita + esquerda
TESTE = 0
if TESTE == 0:
    myTree.build([42, 15, 88, 6, 27, 4]) 
    print(myTree)
    myTree.treeview()

    print('Iterating over tree:')
    for node in myTree:
        print(node,end= ' ')
    print()
elif TESTE == 1:
    myTree.insert(42)
    print(myTree)
    myTree.insert(15)
    print(myTree)
    myTree.insert(88)
    print(myTree)
    myTree.insert(6)
    myTree.insert(27)
    myTree.insert(4)
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
    myTree.insert(120)
    myTree.insert(100)
    myTree.insert(130)
    myTree.insert(80)
    myTree.insert(110)
    myTree.insert(150)
    myTree.insert(200)
    myTree.treeview()
    myTree.traversal()   
elif TESTE == 3:
    myTree.insert(120)
    myTree.insert(110)
    myTree.insert(150)
    myTree.insert(80)
    myTree.insert(130)
    myTree.insert(200)
    myTree.treeview()
    print('\nInserting 100')
    myTree.insert(100) # nó que provoca o balanceamento
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
    myTree.traversal()
    myTree.treeview()



