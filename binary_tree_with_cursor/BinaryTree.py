from typing import List
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

    def insertLeft(self, data:object):
        if self.__left == None:
            self.__left = Node(data)	

    def hasLeftChild(self)->bool:
        return self.__left != None

    def hasRightChild(self)->bool:
        return self.__right != None

    def insertRight(self,data:object):
        if self.__right == None:
            self.__right = Node(data)

    def __str__(self):
        return f'{self.__data}'

        
	    
class BinaryTree:
    '''
    Class that models a basic binary tree.
    Author: Alex Cunha  
    Date of last modification: 27/10/2023
    Attributes
    ----------
    root: reference to the root node.
    cursor: reference to the node where the cursor is located.
            The cursor is used to navigate the tree.
    '''
    preorder  = 0
    inorder   = 1
    postorder = 2

    def __init__(self, data_root:object = None):
        '''
        Initializes the tree with a root node.
        Arguments
        ---------
        data_root (object): the data to be stored in the root node.
        '''
        if data_root is not None:
            self.__root = Node(data_root)
        else:
            self.__root = None
        # O cursor é um apontador usado para navegar na árvore (sem mexer no root)
        self.__cursor = self.__root
    
    def createRoot(self, data:object):
        '''
        Creates the root node of the tree.
        Arguments
        ---------
        data (object): the data to be stored in the root node.
        '''
        if self.__root is None:
            self.__root = Node(data)
            self.__cursor = self.__root


    def isEmpty(self)->bool:
        '''
        Checks if the tree is empty.
        '''
        return self.__root == None

    def height(self)->int:
        '''
        Returns the height of the tree.
        '''
        return self.__height(self.__root)
    
    def __height(self, root:Node)->int:
        if root is None:
            return -1
        else:
            return 1 + max(self.__height(root.left), self.__height(root.right))

    def getRoot(self)->any:
        '''
        Gets the data stored in the root node.
        '''
        return self.__root.data if self.__root != None else None

    def getCursor(self)->any:
        '''
        Gets the data stored in the noted pointed to cursor.
        '''
        return self.__cursor.data if self.__cursor != None else None

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
        if(self.__cursor is not None and self.__cursor.hasLeftChild()): 
            self.__cursor = self.__cursor.left
            
    def downRight(self)->'Node':
        '''
        Moves the cursor to the right child of the node pointed by cursor.
        If there is no right child, don't do anything.
        '''     
        if(self.__cursor is not None and self.__cursor.hasRightChild()): 
            self.__cursor = self.__cursor.right

    def addLeftChild(self, data:object):
        '''
        Adds a new node as the left child of the node pointed by cursor.
        If the cursor has already left child, don't do anything.
        Arguments
        ---------
        data (object): the data to be stored in the new node.
        '''
        if(self.__cursor is not None and not self.__cursor.hasLeftChild()):
            self.__cursor.left = Node(data)

    def addRightChild(self, data:object):
        '''
        Adds a new node as the right child of the node pointed by cursor.
        If the cursor has already right child, don't do anything.
        Arguments
        ---------
        data (object): the data to be stored in the new node.
        '''

        if(self.__cursor is not None and not self.__cursor.hasRightChild()):
            self.__cursor.right = Node(data)

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

    def traversal(self, order:int = None):
        '''
        Print the nodes of the in pre-order, in-order or post-order traversal.
        Arguments
        ---------
        order (int): the order of traversal. The possible values are:
        preorder, inorder, postorder. If no order is given, the traversal
        is performed in pre-order.
        '''
        if order == None:
            self.__preorder(self.__root)
        elif order == self.__class__.preorder:
            self.__preorder(self.__root)
        elif order == self.__class__.inorder:
            self.__inorder(self.__root)
        elif order == self.__class__.postorder:
            self.__postorder(self.__root)
        else:
            raise ValueError('Invalid order value')
        print()
        
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
        self.__cursor = None

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
        # self.__preorderToList(self.__root, result)
        # return ' | '.join(result)
        return self.__preorderToStr(self.__root)[:-2]

    def __preorderToList(self, node:Node, result:List[str]):
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

    
    def treeview(self):
        '''
        Displays the tree in a visual way, in order to understand where
        nodes were inserted.
        '''
        if self.__root is None:
            return
        lines, *_ = self.__visual(self.__root)
        for line in lines:
            print(line)

    def __visual(self, node):
        """
        Returns list of strings, width, height, and horizontal coordinate
        of the root.
        Note: call this method only for small trees.
        """
        # No child.
        if node.right is None and node.left is None:
            line = f'{node.data}'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self.__visual(node.left)
            s = f'{node.data}'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self.__visual(node.right)
            s = f'{node.data}'
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x  = self.__visual(node.left)
        right, m, q, y = self.__visual(node.right)
        s = f'{node.data}'
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2     
    
    def build(self,values:List[any]):
        '''
        Builds a binary tree from a list of values. This method inserts the values
        in the tree in level order. Put None in the list to represent a missing node.
        Precondition: the tree must be empty
        Arguments
        ---------
        values (List[any]): the list of values to be inserted in 
        the tree.

        Example:
        tree = BinaryTree()
        tree.build([1,2,3,4,5,6,7,8,9,10])
        print(tree)
        '''
        if not values or self.__root != None:
            return None 

        self.__root = Node(values[0])
        self.__cursor = self.__root

        # list of nodes to be processed
        node_to_process = [self.__root]
        # index to track the node's position inside the list
        index = 1

        while index < len(values) and node_to_process:
            # remove the first node 
            current_node = node_to_process.pop(0)

            left_value = values[index]
            if left_value is not None:
                current_node.left = Node(left_value)
                node_to_process.append(current_node.left)
            index += 1

            if index < len(values):
                right_value = values[index]
                if right_value is not None:
                    current_node.right = Node(right_value)
                    node_to_process.append(current_node.right)
                index += 1

    def __iter__(self):
        '''
        Returns an iterator for the tree.
        '''
        if self.__root is None:
            self.__stack = []
        else:
            self.__stack = [self.__root]
        return self

    def __next__(self):
        '''
        Returns the next node in the iteration.
        '''
        if not self.__stack:
            raise StopIteration
        node = self.__stack.pop()
        if node.right:
            self.__stack.append(node.right)
        if node.left:
            self.__stack.append(node.left)
        return node.data
    
    def __contains__(self, key:any)->bool:
        '''
        Verifies if a key is present in the tree.
        Method is called when the operator "in" is used.
        '''
        return self.search(key)

 

