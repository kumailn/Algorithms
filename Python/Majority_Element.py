#Question: Given a set of elements, determine what the majority element (occuring more than 50% of the time) if it exists is. You cannot count elements, the only operation available is inputting two items into a tester to check if they're the same or not.
#Difficulty: Divide like mergesort and pass back majority elements up the recussion tree
#Difficulty: Medium

import random
from _DATATYPES import equivalenceTester
def majorityElement(items):
    #Base case, if there is 1 item then it is majority element!
    tester = equivalenceTester()

    if len(items) == 1: return items[0]
    if len(items) == 2: return tester.test(items[0], items[1])

    set2 = items[len(items)//2:]
    set1 = items[:len(items)//2]

    item1 = majorityElement(set1) 
    item2 = majorityElement(set2)

    countLeft = countRight = 0
    for i in items:
        if tester.test(item1, i): countLeft += 1
        if tester.test(item2, i): countRight += 1
    result1 = item1 if countLeft >= len(items) // 2 else None
    result2 = item2 if countRight >= len(items) // 2  else None

    return result1 or result2
                

def main():
    items = ['A', 'B', 'B', 'B', 'C']
    random.shuffle(items)
    print(majorityElement(items))

main()
