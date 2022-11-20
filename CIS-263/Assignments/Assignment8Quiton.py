import math
import time
import random

class minHeap:
    def __init__(self,maxsize, heap=[]):
        self.heap = heap
        self.maxsize = maxsize
        self.size = 0
    
    def insert(self,value):
        if(self.size == 0):
            self.heap.append(value)
            self.size += 1
        else:
            if(self.maxsize != self.size):
                self.size += 1
                self.heap.append(value)
                #check if inserted value is less than parent
                self.heapFix(self.size - 1)
            else:
                #heap full
                print("Heap Full")

    def heapFix(self,index):
        if(index != 2):
            parentIndex = math.floor(index/2)
        else:
            parentIndex = 0
        if(self.heap[index] < self.heap[parentIndex]):
            valueHolder = self.heap[parentIndex]
            self.heap[parentIndex] = self.heap[index]
            self.heap[index] = valueHolder
            self.heapFix(parentIndex)
    
    def sortHeap(self):
        counter = len(self.heap) - 1
        while(counter >= 0):
            self.heapFix(counter)
            counter -= 1

#----testing----
print("----------One by one vs All at once----------")
arrtest = random.sample(range(10000),10000)
arrtest.sort()
##one at a time
start = time.time()
oneByone = minHeap(10000)
for x in arrtest:
    oneByone.insert(x)
executionTime = (time.time() - start)
print("<One at a time>: ", executionTime, "ms")

start = time.time()
allAtonce = minHeap(10000,arrtest)
allAtonce.sortHeap()
executionTime = (time.time() - start)
print("<All at once>:   ", executionTime, "ms")

print("----------Smallest To Largest----------")
#smallest to largest
smallToLarge = random.sample(range(10000),10000)
smallToLarge.sort()

##one at a time
start = time.time()
Small_Large1 = minHeap(10000)
for x in smallToLarge:
    Small_Large1.insert(x)
executionTime = (time.time() - start)
print("Small to largest Execution Time <One at a time>: ", executionTime, "ms")

##all at once
start = time.time()
Small_Large2 = minHeap(10000,smallToLarge)
Small_Large2.sortHeap()
executionTime = (time.time() - start)
print("Small to largest Execution Time <All at once>:   ", executionTime, "ms")

print("----------Largest To Smallest----------")
#largest to smallest
largestTosmallest = random.sample(range(10000),10000)
largestTosmallest.sort(reverse=True)

##one at a time
start = time.time()
Large_Small1 = minHeap(10000)
for x in largestTosmallest:
    Large_Small1.insert(x)
executionTime = (time.time() - start)
print("Largest to smallest Execution Time <One at a time>: ", executionTime, "ms")
##all at once
start = time.time()
Large_Small2 = minHeap(10000,largestTosmallest)
Large_Small2.sortHeap()
executionTime = (time.time() - start)
print("Largest to smallest Execution Time <All at once>:   ", executionTime, "ms") 

print("----------Randomized----------")
#randomized
randomized = random.sample(range(10000),10000)

##one at a time
start = time.time()
randomized1 = minHeap(10000)
for x in randomized:
    randomized1.insert(x)
executionTime = (time.time() - start)
print("randomized Execution Time <One at a time>: ", executionTime, "ms") 

##all at once
start = time.time()
randomized2 = minHeap(10000,randomized)
randomized2.sortHeap()
executionTime = (time.time() - start)
print("randomized Execution Time <All at once>:   ", executionTime, "ms")
