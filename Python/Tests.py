from random import randint
from Insertion_Sort import *

def checkSort(l):
    for i in range(len(l) - 1):
        if(l[i] > l[i + 1]):
            return False
    return True


max = 1000
a = [1, 2, 54, 3, 8, 7, 4, 1, 0]

x = []

for i in range(1000):
    x += [randint(0, max)]

#print(x)
#print(sortInsert(x))

print(checkSort(sortInsert(x)))


