class Knapsack:
    def __init__(self,size=0):
        self.size = size
        self.values = []
        self.weights = []
    
    def addItem(self,inputTextfile):
        f = open(inputTextfile)
        for line in f:
            strline = line.split()
            self.values.append(int(strline[0]))
            self.weights.append(int(strline[1]))
    
    def findMaxvalue(self): #finds the maxvalue
        sackSize = self.size
        itemValues = self.values
        itemWeights = self.weights
        numItems = len(itemValues)
        knapSack = [[0 for weight in range(sackSize + 1)] for item in range(numItems + 1)]
        for item in range(numItems + 1):
            for sackWeight in range(sackSize + 1):
                if item == 0 or sackWeight == 0:
                    knapSack[item][sackWeight] = 0
                elif itemWeights[item - 1] <= sackWeight:
                    knapSack[item][sackWeight] = max(itemValues[item - 1] + knapSack[item-1][sackWeight - itemWeights[item - 1]], knapSack[item-1][sackWeight])
                else:
                    knapSack[item][sackWeight] = knapSack[item - 1][sackWeight]
        maxValue = knapSack[numItems][sackSize]
        print("Knapsack Size: " + str(sackSize))
        print("Max value: " + str(maxValue))

        for item in range(numItems, 0, -1): #finds the items in the knapsack with the maxvalue
            if maxValue <= 0:
                break
            if maxValue == knapSack[item - 1][sackSize]:
                continue
            else:
                print("Item weight: " + str(itemWeights[item - 1]), end=" ")
                print(" | value -> " + str(itemValues[item - 1]))

                maxValue -= itemValues[item - 1]
                sackSize -= itemWeights[item - 1]
        return
    
    
        
sack = Knapsack(10000)
sack.addItem("CIS-263/testCode\knapsackText.txt")
sack.findMaxvalue()
sack2 = Knapsack(11)
sack2.addItem("CIS-263/testCode\knapsackText1.txt")
sack2.findMaxvalue()



