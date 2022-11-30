class Node:
    def __init__(self, value):
        #node identifier
        self.value = value
        #node color
        self.color = None
        #adj nodes
        self.neighbors = []
        

class Graph:
    def __init__(self):
        #list of all the nodes in the graph
        self.nodes = []
        #lsit of colors being used
        self.colors = []
        
    
    #add node method
    def insertNode(self,newNode): #add conectors here
        #add node to graph
        
        self.nodes.append(newNode)
        
        
    
    def addConnections(self,node,connectors):
        if len(connectors) == 0:
            return
        else:
            for value in connectors:
                for gnode in self.nodes:
                    if(value == gnode.value):
                        node.neighbors.append(gnode)
                        break
        

    
    #printgraph
    def displayGraph(self):
        for node in self.nodes:
            print(node.value,end=" ")
            neighbors = []
            for neighbor in node.neighbors:
                neighbors.append(neighbor.value)
            print("connections: " + str(neighbors))

    #graphcolor method
    def colorGraph(self,starting_node):
        #pick any random vertex to start with
        #if list of colors is zero add new color
        #else{
        # check all colors to make sure they aren't the neighboring nodes color
        # }
        return


newGraph = Graph()
nodes = []
connections = [["B","C"],["A","C"],["A","B"]]
start = ord('a')
for letter in range(97,104):
    newNode = Node(chr(letter))
    newGraph.insertNode(newNode)




# newGraph.addConnections(node1, ["B","C"])
# newGraph.addConnections(node2, ["A","C"])
# newGraph.addConnections(node3, ["A","B"])
newGraph.displayGraph()