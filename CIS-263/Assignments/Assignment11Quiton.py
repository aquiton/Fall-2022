class Node():
    def __init__(self,value):
        self.value = value
        self.pointedTo = []
        self.pipeCosts = {}
    
    def addConnection(self, node, pipeCost):
        self.pointedTo.append(node)
        self.pipeCosts[node.value] = pipeCost

class Graph():
    def __init__(self):
        self.sourceNode = Node("source")
        self.sinkNode = Node("sink")
        self.nodes = []
        self.flowGraph = []
        self.nodes.append(self.sourceNode)
        self.nodes.append(self.sinkNode)    

    def addNode(self,value):
        newNode = Node(value)
        self.nodes.append(newNode)
    
    def connectNodes(self,node, pointedTo, pipeCost):
        for gnode in self.nodes:
            if(gnode.value == node):
                snode = gnode
                break
        for gnode in self.nodes:
            if(gnode.value == pointedTo):
                dnode = gnode
                break
        snode.addConnection(dnode,pipeCost)    

    def getAllpaths(self):
        pathlist = []
        route = []
        allpaths = self.calculateAllpaths(self.sourceNode,pathlist,route)
        return allpaths
    
    def calculateAllpaths(self,starting_node,paths,path):
        for node in starting_node.pointedTo:
            if node.value == "sink":
                path.append(node)
                paths.append(path)
                continue
            else:
                path.append(node)
                self.calculateAllpaths(node,paths,path)
            path = []
            path.append(starting_node)
        return paths
    
    def findBestpath(self):
        allpaths = self.getAllpaths()
        allCostsandPaths = []
        for path in allpaths:
            pathCost = []
            dict = {}
            for node in path:
                keys = list(node.pipeCosts)
                for vertex in path:
                    if(vertex.value in keys):
                        pathCost.append(node.pipeCosts[vertex.value])
            pathCost.sort()
            dict["Path"] = path
            dict["Cost"] = pathCost
            allCostsandPaths.append(dict)
        lowestPipecost = allCostsandPaths[0]["Cost"][0]
        highestPath = None
        bestpath = []
        for dict in allCostsandPaths:
            if(dict["Cost"][0] > lowestPipecost):
                lowestPipecost = dict["Cost"][0]
                highestPath = dict
        bestpath.append(lowestPipecost)
        bestpath.append(highestPath)
        return bestpath

    def ford_fulkerson(self):
        flows = self.findBestpath()
        maxflow = 0
        while(flows[0] != 0):
            for node in flows[1]["Path"]:
                keys = list(node.pipeCosts.keys())
                for vertex in flows[1]["Path"]:
                    if(vertex.value in keys):
                        self.changePipecost(node,vertex,flows[0])
            maxflow += flows[0]
            flows = []
            flows = self.findBestpath()
        print("Max Flow: " + str(maxflow))
        
    def changePipecost(self,starting_node,pointedTo,value):
        starting_node.pipeCosts[pointedTo.value] -= value
        return

    def displayGraph(self):
        for node in self.nodes:
            print("Node: " + str(node.value),end = " -> Connection & Costs:")
            print(node.pipeCosts)

fordGraph = Graph()
valName = ["a","b","c","d"]
for value in valName:
    fordGraph.addNode(value)
fordGraph.connectNodes("source","a",4)
fordGraph.connectNodes("source","b",2)
fordGraph.connectNodes("a","b",1)
fordGraph.connectNodes("a","d",4)
fordGraph.connectNodes("a","c",2)
fordGraph.connectNodes("b","d",2)
fordGraph.connectNodes("c","sink",3)
fordGraph.connectNodes("d","sink",3)
print("-----Graph Connections-----")
fordGraph.displayGraph()
fordGraph.ford_fulkerson()
