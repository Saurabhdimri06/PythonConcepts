## Do following Operations on BST
# Find Min val
# Find Max val
# Calculate Sum
# Pre-Order Traversal
# Post-Order Traversal\

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
    
    # Find Max Number
    def maxNumber(self):
        if self.right:
           ans = self.right.maxNumber()
        else:
            ans = self.data
        return ans 
    
    # Find Min Number
    def minNumber(self):
        if self.left:
            ans = self.left.minNumber()
        else:
            ans = self.data
        return ans
    
    # Calculate Sum
    def sumTree(self):
        sum = 0
        sortedBST = self.inOrderTraversal()
        for i in range(0, len(sortedBST)):
            sum += sortedBST[i]
        return sum
    
    # Pre-Order Traversal
    def preOrderTraversal(self):
        elements = []
        #Root, Left, Right
        elements.append(self.data)
        if self.left:
            elements += self.left.preOrderTraversal()
        if self.right:
            elements += self.right.preOrderTraversal()
        
        return elements
    
    def postOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.postOrderTraversal()
        if self.right:
            elements += self.right.postOrderTraversal()
        elements.append(self.data)
        return elements
        
def buildTree(elements):
    
    root = BinarySearchTree(elements[0])
    for i in range (1, len(elements)):
        root.addMember(elements[i])
    
    return root

arr = [4, 7, 9, 12, 17, 18, 20, 26, 32, 45]
bstTree = buildTree(arr)

print("Maximum Number in Tree is: ", bstTree.maxNumber())
print("Minimum Number in Tree is: ", bstTree.minNumber())
print("Sum of Nodes: ", bstTree.sumTree())

print("In Order Traversal: ", bstTree.inOrderTraversal())
print("Pre Order Traversal: ", bstTree.preOrderTraversal())
print("Post Order Traversal: ", bstTree.postOrderTraversal())