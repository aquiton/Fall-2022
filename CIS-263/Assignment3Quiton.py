class singleNode:
    def __init__(self,data = None):
        self.data = data
        self.next = None
    
    def setNext(self, nextNode):
        self.next = nextNode

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addNode(self, data):
        newNode = singleNode(data)
        if(self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def displaylist(self):
        pointer = self.head
        if(self.head == None):
            print("list is empty")
            return
        print("single linked list: ", end = "")
        while(pointer != None):
            print(pointer.data, end = " ")
            pointer = pointer.next

class doubleNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
    def setNext(self, nextNode):
        self.next = nextNode
    
    def setPrev(self, prevNode):
        self.prev = prevNode

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def addNode(self,data):
        newNode = doubleNode(data)
        if(self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
    
    def displaylist(self):
        pointer = self.head
        if(self.head == None):
            print("list is empty")
            return
        print("double linked list: ", end = "")
        while(pointer != None):
            print(pointer.data, end = " ") 
            pointer = pointer.next

#SinglyLinkedList Swap
singleList = SinglyLinkedList()
singleList.addNode(3)
singleList.addNode(5)
singleList.addNode(7)
singleList.addNode(9)
singleList.addNode(11)
singleList.addNode(13)
print("---- Singly Linked List ----")
singleList.displaylist()
print("")
current = singleList.head

while(current != None):
    if(current.data == 7):
        nodeHolder = current
    if(current.data == 9):
        nodeHolder2 = current
    if(current.data == 11):
        nodeHolder3 = current
    if(current.data == 13):
        nodeHolder4 = current
    current = current.next

nodeHolder.setNext(nodeHolder3)
nodeHolder2.setNext(nodeHolder4)
nodeHolder3.setNext(nodeHolder2)
singleList.displaylist()
print("")

#DoublyLinkedList swap
doubleList = DoublyLinkedList()
doubleList.addNode(3)
doubleList.addNode(5)
doubleList.addNode(7)
doubleList.addNode(9)
doubleList.addNode(11)
doubleList.addNode(13)
print("---- Doubly Linked List ----")
doubleList.displaylist()
print("")
current = doubleList.head
while(current != None):
    if(current.data ==  9):
        nodeHolder1 = current
        nodeHolder1prev = nodeHolder1.prev #7
        nodeHolder1next = nodeHolder1.next #11
    if(current.data == 11):
        nodeHolder2 = current
        nodeHolder2prev = nodeHolder2.prev #9
        nodeHolder2next = nodeHolder2.next #13
    current = current.next

nodeHolder1prev.setNext(nodeHolder2)
nodeHolder1.setNext(nodeHolder2next)
nodeHolder1.setPrev(nodeHolder2)
nodeHolder2.setNext(nodeHolder1)
nodeHolder2.setPrev(nodeHolder1prev)
nodeHolder2next.setPrev(nodeHolder1)
doubleList.displaylist()
print("")

#Stacks
print("---- Stack ----")
stack = []
print(stack)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

#Queues
print("---- Queue ----")
queue = []
print(queue)
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)
