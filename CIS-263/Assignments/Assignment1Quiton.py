def insertionsort():
    userinput = []
    while(len(userinput) < 5):
        integer = input("Enter an integer: ")
        userinput.append(int(integer))
        for integer in range(1,len(userinput)):
            key = userinput[integer]
            i = integer - 1
            while i >=0 and key < userinput[i]:
                userinput[i+1] = userinput[i]
                i -= 1
            userinput[i+1] = key
        print(userinput)
   

insertionsort()

