import math
import time
print("---- code1(a) ----")
def code1(n):
    someVariable = 1
    start_time = time.time()
    for x in range(n):
        someVariable = math.log(someVariable) + 3
    print("Time: ", (time.time() - start_time) * 10**3, "ms")
        
#Had to use bigger n values than the other chunks of code
#because the time output would all print as 0.0 ms
code1(10000)
code1(20000)
code1(30000)
code1(40000)
code1(50000)
code1(60000)
code1(70000)
code1(80000)
code1(90000)
code1(100000)

print("---- code2(b) ----")
def code2(n):
    someVariable = 1
    start_time = time.time()
    for i in range(n):
        for j in range(n):
            someVariable = math.log(someVariable) + 3
    print("Time: ", (time.time() - start_time) * 10**3, "ms")

code2(100)
code2(200)
code2(300)
code2(400)
code2(500)
code2(600)
code2(700)
code2(800)
code2(900)
code2(1000)

print("---- code3(c) ----")
def code3(n):
    someVariable = 1
    start_time = time.time()
    for i in range(n):
        for j in range(i):
            someVariable = math.log(someVariable) + 3
    print("Time: ", (time.time() - start_time) * 10**3, "ms")

code3(100)
code3(200)
code3(300)
code3(400)
code3(500)
code3(600)
code3(700)
code3(800)
code3(900)
code3(1000)

print("---- code4(d) ----")
def code4(n):
    someVariable = 1
    start_time = time.time()
    for i in range(n):
        for j in range(i):
            if(j%2 == 0):
                someVariable = math.log(someVariable) + 3
    print("Time: ", (time.time() - start_time) * 10**3, "ms")

code4(100)
code4(200)
code4(300)
code4(400)
code4(500)
code4(600)
code4(700)
code4(800)
code4(900)
code4(1000)


