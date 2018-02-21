from random import randint
from Insertion_Sort import *

max = 1000
a = [1, 2, 54, 3, 8, 7, 4, 1, 0]

x = []

for i in range(4):
    x += [randint(0, max)]

print(x)
print(sortInsert(x))
