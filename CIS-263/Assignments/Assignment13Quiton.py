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
        tempNode = None
        for gnodes in self.nodes:
            if(node == gnodes.value):
                tempNode = gnodes
        if len(connectors) == 0:
            return
        else:
            for value in connectors:
                for gnode in self.nodes:
                    if(value == gnode.value):
                        tempNode.neighbors.append(gnode)
                        break
        
    #printgraph
    def displayGraph(self):
        for node in self.nodes:
            print("Node: " + str(node.value),end=" ")
            print("Color: " + str(node.color),end=" ")
            neighbors = []
            for neighbor in node.neighbors:
                neighbors.append(neighbor.value)
            print("Connections: " + str(neighbors))

    #graphcolor method
    def colorGraph(self):
        colorindex = 0
        for node in self.nodes:
            if len(self.colors) == 0:
                colorindex += 1
                node.color = colorindex
                self.colors.append(1)
            else:
                newColor = False
                sameColor = False
                for color in self.colors:
                    for neighbor in node.neighbors:
                        if(neighbor.color == color):
                            sameColor = False
                            break
                        else:
                            sameColor = True
                    if(sameColor):
                        node.color = color
                        newColor = False
                        break
                    else:
                        newColor = True
                if(newColor):
                    colorindex += 1
                    self.colors.append(colorindex)
                    node.color = colorindex
    
    def colorGraphlimit(self,colorlimit):
        if(colorlimit == 0):
            print("Zero colors")
            return
        colorindex = 0
        for node in self.nodes: #---fix color limit            
            if len(self.colors) == 0:
                colorindex += 1
                node.color = colorindex
                self.colors.append(1)
            else:
                newColor = False
                sameColor = False
                for color in self.colors:
                    for neighbor in node.neighbors:
                        if(neighbor.color == color):
                            sameColor = False
                            break
                        else:
                            sameColor = True
                    if(sameColor):
                        node.color = color
                        newColor = False
                        break
                    else:
                        newColor = True
                if(newColor):
                    colorindex += 1
                    if(colorindex > colorlimit):
                        print("Color Limit: " + str(colorlimit))
                        print("Colors used:" + str(self.colors))
                        colorNodes = []
                        for node in self.nodes:
                            if(node.color != None):
                                colorNodes.append(node)
                        print("Amount of nodes in graph: " + str(len(self.nodes)))
                        print("Amount of nodes colored: " + str(len(colorNodes)))
                        print("Nodes colored: ")
                        for colored in colorNodes:
                            print(str(colored.value) + " -> " + str(colored.color))
                        print("Can't be colored with " + str(colorlimit) + " colors")
                        return False
                    self.colors.append(colorindex)
                    node.color = colorindex
        print("Color Limit: " + str(colorlimit))
        print("Colors used: " + str(self.colors))
        colorNodes = []
        for node in self.nodes:
            if(node.color != None):
                colorNodes.append(node)
        print("Amount of nodes in graph: " + str(len(self.nodes)))
        print("Amount of nodes colored: " + str(len(colorNodes)))
        print("Nodes colored: ")
        for colored in colorNodes:
            print(str(colored.value) + " -> " + str(colored.color))
        print("Can be colored with " + str(colorlimit) + " colors")
        return True


