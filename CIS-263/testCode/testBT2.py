class BTNode:
    def __init__(self):
        self.key = []
        self.c = []
        self.leaf = False
        self.n = 0
    
class BTree:
    def __init__(self, t):
        x = BTNode()
        x.leaf = True
        x.n = 0
        self.root = x
        self.t = t
    
    def splitChild(self,x, i):
        z = BTNode()
        y = x.c[i]
        z.leaf = y.leaf
        z.n = self.t - 1
        for j in range(self.t - 1):
            z.key[j] = y.c[j+self.t]
        y.n = self.t - 1
        for j in range(x.n, i, -1):
            x.c[j+1] = x.c[j]
        x.c[i+1] = z
        for j 
