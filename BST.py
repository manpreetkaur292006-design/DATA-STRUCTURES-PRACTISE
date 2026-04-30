class Node:
    def __init__(self, data):
        self.data = data     
        self.left = None     
        self.right = None    
class BST:
    def __init__(self):
        self.root = None   
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)   
        else:
            self._insert(self.root, data)
    def _insert(self, node, data):
        if data < node.data:        
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:                       
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)
    def inorder(self, node):
        if node:
            self.inorder(node.left)     
            print(node.data, end=" ")   
            self.inorder(node.right)    
tree = BST()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
print("Inorder Traversal:")
tree.inorder(tree.root)