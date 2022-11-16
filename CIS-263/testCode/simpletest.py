x = [1]
print(x)
if(2 not in x):
    print("2 is not in adding 2")
    x.insert(0,2)
    print(x)
else:
    print('2 is already in')

print("removing 2")
x.remove(x[0])
print(x)