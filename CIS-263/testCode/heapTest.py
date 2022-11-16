import math
import random
#heap = [5,4,3,2,1,0,10,12,14,15,16,20,30,22,80,100,900,400,420]

heap = random.sample(range(25),25)

testHeap = [0,1,2,3,5,4]


def swap(index):
    if(index != 2):
        parentIndex = math.floor(index/2)
    else:
        parentIndex = 0
    if(heap[index] < heap[parentIndex]):
        valueHolder = heap[parentIndex]
        heap[parentIndex] = heap[index]
        heap[index] = valueHolder
        swap(parentIndex)
    print("end")

# print(heap)
# swap(5)
# print(heap)
# swap(5)
# print(heap)
# swap(5)
# print(heap)
# swap(4)
# print(heap)
# swap(4)
# print(heap)
# swap(3)
# print(heap)
# swap(2)
# print(heap)


def heapFix(index):
    if(index != 2):
        parentIndex = math.floor(index/2)
    else:
        parentIndex = 0
    if(heap[index] < heap[parentIndex]):
        valueHolder = heap[parentIndex]
        heap[parentIndex] = heap[index]
        heap[index] = valueHolder
        heapFix(parentIndex)

print(heap)
counter = len(heap) - 1
while(counter >= 0):
    heapFix(counter)
    counter -= 1

print("------------END-----------")
print(heap)
print(heap[18])
print(heap[9])
counter = len(heap) - 1
while(counter >= 0):
    heapFix(counter)
    counter -= 1
print("------------END-----------")
print(heap)
print(heap[18])
print(heap[9])
