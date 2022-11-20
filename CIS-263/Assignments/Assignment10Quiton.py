class node():
    def __init__(self,value):
        self.value = value
        self.pointedTo = []
    
    def displayPointedTo(self):
        print(str(self.value) + " is pointed to [",end="")
        for node in self.pointedTo:
            print(node.value,end=" ")
        print("]")

class graph():
    def __init__(self,value):
        self.root = node(value)
        self.vertcies = [self.root]

    def insert(self, value):
        for vertex in self.vertcies:
            if(vertex.value == value):
                print(str(value) + " is already in graph")
                return
        newNode = node(value)
        self.vertcies.append(newNode)

    def displayVertcies(self):
        print("[",end="")
        for vertex in self.vertcies:
            print(vertex.value,end=" ")
        print("]")

    def getVertex(self,value):
        for vertex in self.vertcies:
            if vertex.value == value:
                return vertex
        print(str(value) + " is not in graph")
        
    def addConnection(self,inputvertex,inputpointer):
        nodeVertex = None
        nodePointer = None
        for vertex in self.vertcies:
            if vertex.value == inputvertex:
                nodeVertex = vertex
                break
        for pointer in self.vertcies:
            if pointer.value == inputpointer: 
                nodePointer = pointer
                break
        if nodeVertex and nodePointer not in self.vertcies:
            print("Vertcies not in graph")
            return
        if nodeVertex in nodePointer.pointedTo:
            print(str(nodePointer.value) + " is already pointing at " + str(nodeVertex.value))
            return
        if nodePointer in nodeVertex.pointedTo:
            print(str(nodePointer.value) + " Already connected")
            return
        nodeVertex.pointedTo.append(nodePointer)
    
    def DFS(self,dvertex,fvertex):
        for vertex1 in fvertex.pointedTo:
            if vertex1 == dvertex:
                print(vertex1.value, end= " <- ")
                return 1
            else:
                temp = self.DFS(dvertex,vertex1)
                if temp == 1:
                    print(vertex1.value,end = " <- ")
                    return 1
        return 0

    def BFS(self,dvertex,fvertex):
        visited = []
        queue = []
        visited.append(fvertex.value)
        queue.append(fvertex)

        while queue:
            vert = queue.pop(0)
            print(vert.value, end = " ")

            for neighbour in vert.pointedTo:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
            if vert == dvertex:
                print("Found: " + str(dvertex.value))
                return
        print("[" + str(dvertex.value) + "]" + " is not in graph or is not connected")
    
    def topologicalsort(self,vertex):
        visited = []
        visited = self.quickDFS(vertex,visited)
        visited.reverse()
        for x in visited:
            print(x.value, end=" ")
        return
    
    def quickDFS(self,starting_vertex,visited):
        for vertex in starting_vertex.pointedTo:
            if(len(vertex.pointedTo) == 0):
                if(vertex not in visited):
                    visited.append(vertex)
            else:
                self.quickDFS(vertex,visited)
        if(starting_vertex not in visited):
            visited.append(starting_vertex)
        return visited
    
    def stronglyConnected(self):
    
        visted = []
        for vertex in self.vertcies:
            visted.append(vertex.value)
            tempConnected = []
            for vertex1 in self.vertcies:
                for pointer in vertex1.pointedTo:
                    if(vertex.value == pointer.value and vertex1.value not in visted):
                        tempConnected.append(vertex.value)
                        tempConnected.append(vertex.pointedTo[0].value)
                        tempConnected.append(vertex1.value)
                        break
          
            if(len(tempConnected) > 0):
                print(str(vertex.value) + ": " + str(tempConnected))


    
    
                    

        
    
   


        
        
        

            

                
                


#creating edges and vertices
newGraph = graph(1)
for value in range(2,14):
    newGraph.insert(value)
print("Vertcies in graph: ", end="")
newGraph.displayVertcies()
newGraph.addConnection(1, 2)
newGraph.addConnection(1, 3)
newGraph.addConnection(2, 4)
newGraph.addConnection(2, 5)
newGraph.addConnection(3, 6)
newGraph.addConnection(3, 7)
newGraph.addConnection(4, 10)
newGraph.addConnection(5, 11)
newGraph.addConnection(6, 8)
newGraph.addConnection(7, 9)
newGraph.addConnection(8, 12)
newGraph.addConnection(9, 12)
newGraph.addConnection(10, 12)
newGraph.addConnection(11, 12)
#displaying graph
print("----Connections----")
for vertex in newGraph.vertcies:
    vertex.displayPointedTo()

#depth first search
print("-----DFS-----")
dfs = newGraph.getVertex(12)
dfs1 = newGraph.getVertex(9)
dfs2 = newGraph.getVertex(13)
dfsroot = newGraph.getVertex(1)

#searching for vertex 12
print("Searching for: [" + str(dfs.value), end="] ")
output = newGraph.DFS(dfs,dfsroot)
if(output == 0):
    print("Value you are looking for is either not in the graph or is not connected to anything")
else: 
    print(str(dfsroot.value) + " PATH FOUND!")

#searching for vertex 9
print("Searching for: [" + str(dfs1.value), end="] ")
output = newGraph.DFS(dfs1,dfsroot)
if(output == 0):
    print("Value you are looking for is either not in the graph or is not connected to anything")
else: 
    print(str(dfsroot.value) + " PATH FOUND!")

#searching for vertex (13) not connected in graph
print("Searching for: [" + str(dfs2.value), end="] ")
output = newGraph.DFS(dfs2,dfsroot)
if(output == 0):
    print("Value you are looking for is either not in the graph or is not connected to anything")
else: 
    print(str(dfsroot.value) + " PATH FOUND!")

#breadth first search
print("-----BFS-----")
bfs = newGraph.getVertex(12)
bfs1 = newGraph.getVertex(7)
bfs2 = newGraph.getVertex(13)
bfsroot = newGraph.getVertex(1)
newGraph.BFS(bfs,bfsroot)
newGraph.BFS(bfs1,bfsroot)
newGraph.BFS(bfs2,bfsroot)

print("-----Topologicalsort-----")
root = newGraph.getVertex(1)
newGraph.topologicalsort(root)

#strongly connected
print()
print("-----Strongly Connected-----")
scGraph = graph(1)
for value in range(2,14):
    scGraph.insert(value)
scGraph.addConnection(1,2)
scGraph.addConnection(1,3)
scGraph.addConnection(2,4)
scGraph.addConnection(3,6)
scGraph.addConnection(4,8)
scGraph.addConnection(4,5)
scGraph.addConnection(6,10)
scGraph.addConnection(6,7)
scGraph.addConnection(5,2)
scGraph.addConnection(7,3)
scGraph.addConnection(8,9)
scGraph.addConnection(10,11)
scGraph.addConnection(9,12)
scGraph.addConnection(12,8)
scGraph.displayVertcies()
for vertex in scGraph.vertcies:
    vertex.displayPointedTo()
print("Strongly connected: ")
scGraph.stronglyConnected()
