class Node:
    '''
    Classe that models a dinamic node of a binary tree.
    '''
    def __init__(self,data:object):
        '''
        Constructor that initializes a node with a data and
        without children.'''
        self.__data = data
        self.__left = None
        self.__right = None
        self.__parent = None

    @property
    def data(self)->object:
        return self.__data

    @data.setter
    def data(self, newData:object):
        self.__data = newData

    @property
    def left(self)->'Node':
        return self.__left

    @left.setter
    def left(self, newLeftChild:object):
        self.__left = newLeftChild

    @property
    def right(self)->'Node':
        return self.__right

    @right.setter
    def right(self, newRightChild:'Node'):
        self.__right = newRightChild

    @property
    def parent(self)->'Node':
        return self.__parent

    @parent.setter
    def parent(self, newParent:'Node'):
        self.__right = newParent

    def addLeft(self, data:object):
        if self.__left == None:
            node = Node(data)
            node.__parent = self
            self.__left = node	

    def hasLeftChild(self)->bool:
        return self.__left != None

    def hasRightChild(self)->bool:
        return self.__right != None

    def addRight(self,data:object):
        if self.__right == None:
            node = Node(data)
            node.__parent = self
            self.__right = node

    def __str__(self):
        return f'{self.__data}'

        
	    
class BinaryTree:
    '''
    Class that models a basic binary tree with link to ancestor node.
    Author: Alex Cunha  
    Date of last modification: 31/10/2023
    Attributes
    ----------
    root: reference to the root node.
    cursor: reference to the node pointed by cursor.
    '''
    def __init__(self, data_root:object):
        '''
        Initializes the tree with a root node.
        Arguments
        ---------
        data_root (object): the data to be stored in the root node.
        '''
        self.__root = Node(data_root)
        self.__cursor = self.__root

    def isEmpty(self)->bool:
        '''
        Checks if the tree is empty.
        '''
        return self.__root == None
    
    def getRoot(self)->'Node':
        '''
        Gets the data stored in the root node.
        '''
        return self.__root.data if self.__root != None else None

    def getCursor(self)->'Node':
        '''
        Gets the data stored in the noted pointed to cursor.
        '''
        return self.__cursor.data if self.__cursor != None else None

    def back(self):
        ''' 
        Moves the cursor to the parent node.
        '''
        self.__cursor = self.__cursor.parent if self.__cursor.parent != None else self.__cursor

    def reset(self):
        ''' 
        Resets the cursor to the root node.
        '''
        self.__cursor = self.__root

    def downLeft(self)->'Node':
        '''
        Moves the cursor to the left child of the node pointed by cursor.
        If there is no left child, don't do anything.
        '''
        if(self.__cursor.hasLeftChild()): 
            self.__cursor = self.__cursor.left
            
    def downRight(self)->'Node':
        '''
        Moves the cursor to the right child of the node pointed by cursor.
        If there is no right child, don't do anything.
        '''     
        if(self.__cursor.hasRightChild()): 
            self.__cursor = self.__cursor.right

    def addLeftChild(self, data:object):
        '''
        Adds a new node as the left child of the node pointed by cursor.
        If the cursor has already left child, don't do anything.
        Arguments
        ---------
        data (object): the data to be stored in the new node.
        '''
        if(not self.__cursor.hasLeftChild()):
            self.__cursor.addLeft(data)

    def addRightChild(self, data:object):
        '''
        Adds a new node as the right child of the node pointed by cursor.
        If the cursor has already right child, don't do anything.
        Arguments
        ---------
        data (object): the data to be stored in the new node.
        '''
        if(not self.__cursor.hasRightChild()):
            self.__cursor.addRight(data)

    def __len__(self)->int:
        '''
        Counts the number of nodes in the tree.
        '''
        return self.__count(self.__root)

    def __count(self, root:Node)->int:
        if root is None:
            return 0
        else:
            return 1 + self.__count(root.left) + self.__count(root.right)


    def search(self, key:object )->bool:
        '''
        Perform a search in the tree for a node with the given key
        Returns
        -------
        True: if the key is found in the tree.
        False: if the key is not found in the tree.
        '''
        return self.__searchData(key, self.__root)
    
    def __searchData(self, key:any, node:Node)->bool:
        if (node == None):
            return False # Nao encontrou a chave
        if ( key == node.data):
            return True
        elif ( self.__searchData( key, node.left)):
            return True
        else:
            return self.__searchData( key, node.right)

    def preorder(self):
        '''
        Displays the nodes of the tree in pre-order traversal.
        '''
        self.__preorder(self.__root)

    def inorder(self):
        '''
        Displays the nodes of the tree in in-order traversal.
        '''
        self.__inorder(self.__root)

    def postorder(self):
        '''
        Displays the nodes of the tree in post-order traversal.
        '''
        self.__postorder(self.__root)
        
    def __preorder(self, node):
        if( node is not None):
            print(f'{node.data} ',end='')
            self.__preorder(node.left)
            self.__preorder(node.right)

    def __inorder(self, node):
        if( node is not None):
            self.__inorder(node.left)
            print(f'{node.data} ',end='')
            self.__inorder(node.right)

    def __postorder(self, node):
        if( node is not None):
            self.__postorder(node.left)
            self.__postorder(node.right)
            print(f'{node.data} ',end='')

    def clear(self):
        '''
        Deletes all nodes of the tree.
        '''
        self.__root = None

    # o cursor tem que estar posicionado no nó pai
    # do nó que vai ser removido
    def delete(self, key:object):
        '''
        Delete the node that matches with key argument.
        IMPORTANT:
        a) the cursor must be positioned at the parent node of the key node.
        b) if it cannot be removed (empty tree, cursor in the wrong place, ...)
           no action is taken.
        '''
        if self.__root is None:
            return
        elif self.__root.data == key:
            if self.__root.left == None and self.__root.right == None:
                self.__cursor = self.__root = None
        else:
            self.__deleteNode(self.__cursor, key)

    def __deleteNode(self,root, key):
        if root.left == None and root.right == None: # leaf node
            return
        
        if root.left == None:
            if root.right.data == key:
                root.right = None
        elif root.right == None:
            if root.left.data == key:
                root.left = None
    
    def __str__(self)->str:
        '''
        Returns a string representation of the tree in preorder traversal.
        '''
        # result = []
        # self.__preorderToString(self.__root, result)
        # return ' | '.join(result)
        return self.__preorderToStr(self.__root)

    def __preorderToString(self, node:Node, result:str):
        if node is not None:
            result.append(str(node.data))
            self.__preorderToString(node.left, result)
            self.__preorderToString(node.right, result)

    def __preorderToStr(self, root)->str:
        if (root is None):
            return ''
    
        result = str(root.data) + ' | '
        result += self.__preorderToStr(root.left)
        result += self.__preorderToStr(root.right)
        return result

