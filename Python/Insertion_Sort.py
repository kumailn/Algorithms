#Insertion sort implementation in Python
def sortInsert(inputList):
    print(inputList)
    #Start from second item (because first item is already inserted correctly)
    for i in range(1, len(inputList)):
        j = i
        #As long as the item before is larger than the current item
        while(j > 0 and inputList[j] < inputList[j - 1]):
            #print("Iteration: ", inputList)
            #Save current item as temp
            temp = inputList[j]
            #Change current item to previous item
            inputList[j] = inputList[j - 1]
            #Change previous item to saved temp item
            inputList[j-1] = temp
            #Decrement i
            j = j - 1
    return inputList


a = [7, 8, 3, 4, 2, 1, 0]
sortInsert(a)
print(a)
