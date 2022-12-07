import unittest
import sys
sys.path.insert(1,'C:/Users/aquit/Documents/GitHub/Programming Journey/Fall-2022/CIS-263/Assignments/')
import Assignment13Quiton as graph

class TestCalc(unittest.TestCase):

    global newGraph
    newGraph = graph.Graph()
    
    def createGraph(self):
        connections = {
        "a": ["b","d","e"],
        "b": ["a","c","d","e"],
        "c": ["b","d"],
        "d": ["a","b","e","f"],
        "e": ["a","b","c","d","f"],
        "f": ["d","e"]
        }
        for letter in range(97,103): # a - f inclusive
            newNode = graph.Node(chr(letter))
            newGraph.insertNode(newNode)
        for node in list(connections.keys()):
            newGraph.addConnections(node,connections[node])
        

    def test_threeColorlimit(self):
        self.createGraph()
        result = newGraph.colorGraphlimit(3)
        self.assertFalse(result)
        newGraph.__init__()
        print("--------------------------")
        #graph should not be able to be colored with 3 colors
    
    def test_fourColorlimit(self):
        self.createGraph()
        newGraph.displayGraph()
        result = newGraph.colorGraphlimit(4)
        self.assertTrue(result)
        newGraph.__init__()
        print("--------------------------")
    
    def test_tenColorlimit(self):
        self.createGraph()
        result = newGraph.colorGraphlimit(10)
        self.assertTrue(result)
        newGraph.__init__()
        print("--------------------------")

if __name__ == '__main__':
    unittest.main()