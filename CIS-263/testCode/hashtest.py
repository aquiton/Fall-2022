#from Assignment9Quiton.py import hashtable

linearTable = hashtable()
for x in range(1,100000):
    linearTable.linearProbing(x)
print(linearTable.collisonCounter)

quadraticTable = hashtable()
for x in range(1,100000):
    quadraticTable.quadraticProbing(x)
print(quadraticTable.collisonCounter)

doublehashTable = hashTable()
for x in range(1,100000):
    doublehashTable.doubleHashing(x)
print(doublehashTable.collisonCounter)