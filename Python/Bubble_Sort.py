def checkSort(l):
    for i in range(len(l) - 1):
        if(l[i] > l[i + 1]):
            return False
    return True

def sortBubble(inputList):
    while(not checkSort(inputList)):
        for i in range(len(inputList) - 1):
            if(inputList[i] > inputList[i + 1]):
                temp = inputList[i]
                inputList[i] = inputList[i + 1]
                inputList[i + 1] = temp
    return(inputList)

a = [7, 8, 3, 4, 2, 1, 0]
sortBubble(a)
print(a)
