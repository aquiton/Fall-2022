class Node:
    def __init__(self, value):
        self.red = False
        self.parent = None
        self.value = value
        self.left = None
        self.right = None
    
class RBTree:
    def __init__(self):
        self.nil = Node(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil
    
    def rbInsert(self, value):
        newNode = Node(value)
        newNode.parent = None
        newNode.left = self.nil
        newNode.right = self.nil
        newNode.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if newNode.value < current.value:
                current = current.left
            elif newNode.value > current.value:
                current = current.right
            else:
                return
        newNode.parent = parent
        if parent == None:
            self.root = newNode
        elif newNode.value < parent.value:
            parent.left = newNode
        else:
            parent.right = newNode
        
        self.rbinsertFixup(newNode)
    
    def rbinsertFixup(self, newNode):
        while newNode != self.root and newNode.parent.red:
            if newNode.parent == newNode.parent.parent.right:
                y = newNode.parent.parent.left
                if y.red:
                    y.red = False
                    newNode.parent.red = False
                    newNode.parent.parent.red = True
                    newNode = newNode.parent.parent
                else:
                    if newNode == newNode.parent.left:
                        newNode = newNode.parent
                        self.rightRotate(newNode)
                    newNode.parent.red = False
                    newNode.parent.parent.red = True
                    self.leftrotate(newNode.parent.parent) 
            else:
                y = newNode.parent.parent.right

                if y.red:
                    y.red = False
                    newNode.parent.red = False
                    newNode.parent.parent.red = True
                    newNode = newNode.parent.parent
                else:
                    if newNode == newNode.parent.right:
                        newNode = newNode.parent
                        self.leftrotate(newNode) 
                    newNode.parent.red = False
                    newNode.parent.parent.red = True
                    self.rightRotate(newNode.parent.parent) 
        self.root.red = False

    def leftrotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    def rbtransplate(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def rbDelete(self, z):
        y = z
        yOGcolor = y.red
        if z.left == self.nil:
            x = z.right
            self.rbtransplate(z,z.right)
        elif z.right == self.nil:
            x = z.left
            self.rbtransplate(z,z.left)
        else:
            y = self.treeMin(z.right) 
            yOGcolor = y.red
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rbtransplate(y,y.right)
                y.right = z.right
                y.right.parent = y
                self.rbtransplate(z,y)
                y.left = z.left
                y.left.parent = y
                y.red = z.red
        if yOGcolor == False:
            self.rbDeleteFixup(x)
    
    def treeMin(self,node):
        current = node
        while current != self.nil:
            current = current.left
        return current 

    def rbDeleteFixup(self, x):
        while x != self.root and x.red != True:
            if x == x.parent.left:
                w = x.parent.right
                if w.red == True:
                    w.red = False
                    x.parent.red = True
                self.leftrotate(x.parent)
                w = x.parent.right
            if w.left.red == False and w.right.red == False:
                w.red = True
                x = x.parent
            elif w.right.red == False:
                w.left.red = False
                w.red = True
                self.rightRotate(w)
                w = x.parent.right
            else:
                w.red = x.parent.red
                x.parent.red = False
                w.right.red = False
                self.leftrotate(x.parent)
                x = self.root
        x.red = False
    
    def __repr__(self):
        lines = []
        print_tree(self.root, lines)
        return '\n'.join(lines)


def print_tree(node, lines, level=0):
    if node.value != 0:
        print_tree(node.left, lines, level + 1)
        lines.append('-' * 4 * level + '> ' +
                     str(node.value) + ' ' + ('r' if node.red else 'b'))
        print_tree(node.right, lines, level + 1)


def main():
    print("Inserted from lowest to highest:")
    input = [26,17,41,14,21,30,47,10,16,19,23,28,38,7,12,15,20,35,39,3]
    input = sorted(input)
    print(input)
    tree = RBTree()
    
    for x in input:
        tree.rbInsert(x)
    print(tree)

    print("---------------------END------------------------")
    print("Insertion sequence for example from assignment:")
    input2 = [26,17,41,14,21,30,47,10,16,19,23,28,38,7,12,15,20,35,39,3]

    print(input2)
    tree = RBTree()
    for x in input2:
        tree.rbInsert(x)
    print(tree)


main()
            



    



    
