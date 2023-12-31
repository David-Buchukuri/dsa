class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        nodeToInsert = Node(value)

        if not self.root:
            self.root = nodeToInsert
            return
        
        parent = self.root

        while True:
            if nodeToInsert.value < parent.value:
                if parent.left:
                    parent = parent.left
                else:
                    parent.left = nodeToInsert
                    return
            else:
                if parent.right:
                    parent = parent.right
                else:
                    parent.right = nodeToInsert
                    return
                

    def find(self, value):
        curr = self.root

        while curr:
            if curr.value == value:
                return value
            elif value < curr.value:
                 curr = curr.left
            else:
                curr = curr.right
    
    def delete(self, value):
        self.root = self.__delete(self.root, value)
       

    def __delete(self, node, key):  
        if not node:
            return
        
        if node.value != key:
            if key < node.value:
                node.left = self.__delete(node.left, key)
            else:
                node.right = self.__delete(node.right, key)
        
            return node
        

        if not node.right:
            return node.left

        if not node.right.left:
            node.right.left = node.left
            return node.right
        
        leftSubTree = node.left
        rightSubTree = node.right
        leftmostOnRight = node.right.left
        prev = node.right

        while leftmostOnRight.left:
            prev = leftmostOnRight
            leftmostOnRight = leftmostOnRight.left
        
        prev.left = leftmostOnRight.right
        leftmostOnRight.left = leftSubTree
        leftmostOnRight.right = rightSubTree
        return leftmostOnRight



    def log(self, node):
        if not node:
            return

        self.log(node.left)
        print(node.value)
        self.log(node.right)


bst = BST()

bst.insert(7)
bst.insert(4)
bst.insert(2)
bst.insert(10)
bst.insert(5)
bst.insert(9)

bst.delete(9)
bst.delete(5)
bst.delete(7)

bst.log(bst.root)
print(bst.find(4))
print(bst.find(29))




        

