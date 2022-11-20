import random
class hashtable:
    def __init__(self):
        self.tableSize = 10001
        self.hashTable = {}
        self.collisonCounter = 0
    
    def hashFunction(self,x):
        return x % 300
    
    def hashFunction2(self,x):
        return 9973 - (x % 9973)

    def linearProbing(self,x):
        inserted = False
        currentSlot = self.hashFunction(x)
        if currentSlot in self.hashTable:
            while inserted == False:
                if currentSlot not in self.hashTable:
                    self.hashTable[currentSlot] = x
                    break
                else:
                    currentSlot = (currentSlot + 1) % self.tableSize #mod by table size
                    self.collisonCounter += 1
        else:
            self.hashTable[currentSlot] = x
        return self.collisonCounter
    
    def quadraticProbing(self,x):
        inserted = False
        currentSlot = self.hashFunction(x)
        index = 1
        if currentSlot in self.hashTable:
            while inserted == False:
                if currentSlot not in self.hashTable:
                    self.hashTable[currentSlot] = x
                    inserted = True
                else:
                    currentSlot = (currentSlot + index**2) % self.tableSize #mod by table size
                    index += 1
                    self.collisonCounter += 1
        else:
            self.hashTable[currentSlot] = x
        return self.collisonCounter
    
    def doubleHashing(self,x):
        inserted = False
        currentSlot = self.hashFunction(x)
        index = 1
        if currentSlot in self.hashTable:
            while inserted == False:
                if currentSlot not in self.hashTable:
                    self.hashTable[currentSlot] = x
                    inserted = True
                else:
                    currentSlot = (currentSlot + index*self.hashFunction2(x)) % self.tableSize #mod by table size
                    self.collisonCounter += 1
        else:
            self.hashTable[currentSlot] = x
        return self.collisonCounter

#testing
randomlist = random.sample(range(1,100000), 500)

#LinearProbing
linearTable = hashtable()
for x in randomlist:
    linearTable.linearProbing(x)
print("-----LinearProbing-----")
print("Number of collisions: " + str(linearTable.collisonCounter))

#QuadraticProbing
quadraticTable = hashtable()
for x in randomlist:
    quadraticTable.quadraticProbing(x)
print("-----QuadraticProbing-----")
print("Number of collisions: " +  str(quadraticTable.collisonCounter))

#DoubleHashing
doublehashTable = hashtable()
for x in randomlist:
    doublehashTable.doubleHashing(x)
print("-----DoubleHashing-----")
print("Number of collisions: " + str(doublehashTable.collisonCounter))