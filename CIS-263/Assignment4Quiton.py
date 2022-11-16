class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        self.isRoot = True
    
    def insert(self, value):
       
        if self.value != None:
            if value < self.value:
                if self.leftChild == None:
                    self.leftChild = Node(value)
                    self.leftChild.isRoot = False
                else:
                    self.leftChild.insert(value)
            elif value > self.value:
                if self.rightChild == None:
                    self.rightChild = Node(value)
                    self.rightChild.inRoot = False
                else:
                    self.rightChild.insert(value)
        else:
            self.value = value
    
    def printTree(self, root=None):
        if self.leftChild:
            self.leftChild.printTree()
        if self.value == root:
            print("[" + str(self.value) + "]", end =" ")
        else:
            print(self.value, end=" ")
        if self.rightChild:
            self.rightChild.printTree()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(13)
root.insert(50)
root.insert(7)
root.insert(75)
root.printTree(root.value)
print("")
print("isRoot: " + str(root.value) + " - " + str(root.isRoot))
print("isRoot: " + str(root.leftChild.value) + " - " + str(root.leftChild.isRoot))

#inorder
print("Inorder Tree Walk: ",end="")
def inorder(root):
    if root != None:
        inorder(root.leftChild)
        print(root.value, end=" ")
        inorder(root.rightChild)
inorder(root)
print("")

#preorder
print("Preorder Tree Walk: ",end="")
def preorder(root):
    if root != None:
        print(root.value, end= " ")
        preorder(root.leftChild)
        preorder(root.rightChild)
preorder(root)
print("")

#postorder
print("Postorder Tree Walk: ", end="")
def postorder(root):
    if root != None:
        postorder(root.leftChild)
        postorder(root.rightChild)
        print(root.value, end=" ")
postorder(root)

testRoot = Node(50)
testRoot1 = Node(40)
testRoot2 = Node(80)
testRoot3 = Node(55)
testRoot4 = Node(60)
testRoot.rightChild = testRoot1
testRoot.leftChild = testRoot2
testRoot1.leftChild = testRoot3
testRoot1.rightChild = testRoot4
print("")

def isTree(root):
    rootPointer1 = root
    rootPointer2 = root
    while rootPointer1.leftChild != None:
        rootPointer1 = rootPointer1.leftChild
        if(rootPointer1.value > root.value):
            return False
    minNode = rootPointer1
    
    while rootPointer2.rightChild != None:
        rootPointer2 = rootPointer2.rightChild
        if(rootPointer2.value < root.value):
            return False
    maxNode = rootPointer2


    if(minNode.value > maxNode.value):
        return False
    else:
        return True

print(isTree(root))
print(isTree(testRoot)) 