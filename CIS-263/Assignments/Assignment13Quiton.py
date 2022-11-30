class Node:
    def __init__(self, value):
        #node identifier
        self.value = value
        #node color
        self.color = None
        #adj nodes
        self.neighbors = []
        return

class Graph:
    def __init(self):
        #list of all the nodes in the graph
        self.nodes = []
        #lsit of colors being used
        self.colors = []
        return
    
    #add node method
    def insertNode(self,node,connectors): #add conectors here
        #add node to graph
        self.nodes.append(node)
        #add adj/connectors
        if len(connectors) == 0:
            return
        else:
            for value in connectors:
                for gnode in self.nodes:
                    if(value == gnode.value):
                        node.neighbors.append(gnode)
                        break
        return
    
    #printgraph
    def displayGraph(self):
        

    #graphcolor method
    def colorGraph(self,starting_node):
        #pick any random vertex to start with
        #if list of colors is zero add new color
        #else{
        # check all colors to make sure they aren't the neighboring nodes color
        # }
        return
