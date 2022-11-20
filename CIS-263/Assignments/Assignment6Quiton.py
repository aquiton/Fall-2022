class BTNode:
    def __init__(self):
        self.keys = [] 
        self.children = []
        self.leaf = False
        
    
class BTree:
    def __init__(self, t):
        x = BTNode()
        x.leaf = True
        self.t = t
        self.root = x
    
    def splitChild(self, node, index):
        newNode = BTNode()
        y = node.children[index-1]
        newNode.leaf = y.leaf
        for value in range(self.t - 1):
                newNode.keys.insert(value,y.keys[value+self.t]) 
        if not y.leaf:
            for child in range(self.t):
                    newNode.children.insert(child,y.children[child+self.t])
        for child in range(len(node.keys)+1, index+1, -1):
            node.children[child+1] = node.children[child]      
        node.children.insert(index+1,newNode)
        for value in range(len(node.keys), index , -1):
            node.keys[value+1] = node.keys[value]
        node.keys.insert(index,y.keys[self.t])
        y.keys.pop(self.t)
        if(len(y.keys) > self.t):
            y.keys.pop(self.t)
        y.keys.pop(0)
        newNode.keys.pop(0)
    
    def insert(self, value):
        oldroot = self.root
        if len(oldroot.keys) == ((self.t * 2) - 1): #root is full
            newNode = BTNode()
            self.root = newNode
            newNode.leaf = False
            newNode.children.insert(1,oldroot)
            self.splitChild(newNode,1)
            self.insertNonFull(newNode,value)
        else:
            self.insertNonFull(oldroot,value) #root isnt full
            
    def insertNonFull(self, node, value):
        i = len(node.keys)
        if node.leaf:
            while i >= 1 and value < node.keys[i-1]:
                node.keys[i+1] = node.keys[i]
                i = i - 1
            node.keys.insert(i+1,value)
        else:
            while i >= 1 and value < node.keys[i-1]:
                i = i - 1
            i = i + 1
            if len(node.children[i-1].keys) == (self.t * 2) - 1:
                self.splitChild(node,i)
                if value > node.keys[i-1]:
                    i = i + 1
            self.insertNonFull(node.children[i-1], value)

    def print_node(self, node, i):
        if i != 0:
            print(node.keys, end="    ")
        
        for x in node.children:
            self.print_node(x, i+1)
            print("",end="")
    
    def printTree(self,node):
        print("Root: ", end="")
        for x in node.children:
            print("    ", end="")
        print(node.keys)
        print()
        print("child: ", end="")
        self.print_node(node,0)
    


def main():
    B = BTree(3)

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for letter in alphabet:
        B.insert(letter)
    print("T = 3:")
    print("------")
    B.printTree(B.root)

    
if __name__ == '__main__':
    main()
    



