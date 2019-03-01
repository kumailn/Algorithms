#Question: Given a set of elements, determine what the majority element (occuring more than 50% of the time) if it exists is. You cannot count elements, the only operation available is inputting two items into a tester to check if they're the same or not.
#Solution: Divide like mergesort and pass back majority elements up the recussion tree
#Difficulty: Medium

import random
from _DATATYPES import equivalenceTester

def majorityElement(items):
    tester = equivalenceTester()

    #Base cases, if there's 1 item left then it is the majority element! If there's two we can see if they're the same using the tester and return that
    if len(items) == 1: return items[0]
    if len(items) == 2: return tester.test(items[0], items[1])

    #Divide the list of items into a left and a right half
    set2 = items[len(items)//2:]
    set1 = items[:len(items)//2]

    #Recurse on the left and right halves 
    item1 = majorityElement(set1) 
    item2 = majorityElement(set2)

    #Once item1 and item2 have been returned up the recursion tree we count the number of occurances of each 
    countLeft = countRight = 0
    for i in items:
        if tester.test(item1, i): countLeft += 1
        if tester.test(item2, i): countRight += 1
    
    #Result1 is set to item1 if item1's count is >= half the items, likewise for result2. Otherwise it's not a majority element and we set it to None
    result1 = item1 if countLeft >= len(items) // 2 else None
    result2 = item2 if countRight >= len(items) // 2  else None

    #Return either of the two, whichever is non-null
    return result1 or result2
                

def main():
    items = ['A', 'B', 'B', 'B', 'C']
    random.shuffle(items)

    #Should return 'B' as that occurs more than half the time
    print(majorityElement(items))

main()
