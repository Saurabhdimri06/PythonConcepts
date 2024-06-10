class BinarySearchTree:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    # Binary Search Tree Add Node. Traversal process from left to right
    def addMember(self, data):
        
        # If data already exists skip
        if data == self.data:
            return
        
        if data < self.data:
            # check if it's leaf node or not. Else add the item
            if self.left:
                self.left.addMember(data)
            else:
                self.left = BinarySearchTree(data)
        
        if data > self.data:
            if self.right:
                self.right.addMember(data)
            else:
                self.right = BinarySearchTree(data)
                
    def inOrderTraversal(self):
        
        elements = []
        
        # Left Traversal, then In Node, then Right Traversal
        if self.left:
            elements += self.left.inOrderTraversal()
            
        elements.append(self.data)
        
        if self.right:
            elements += self.right.inOrderTraversal()
        
        return elements
    
def buildTree(elements):
    
    root = BinarySearchTree(elements[0])
    for i in range (1, len(elements)):
        root.addMember(elements[i])
    
    return root

arr = [17, 18, 20, 4, 7, 26, 9, 32, 45, 12]
bstTree = buildTree(arr)

inTraversal = bstTree.inOrderTraversal()
print(inTraversal)