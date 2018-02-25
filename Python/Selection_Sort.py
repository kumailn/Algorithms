def sortSelection(inputList):
    for i in range(len(inputList)):
        min = i+1
        for j in range(i, len(inputList)):
            if(inputList[j] < min):
                min = j
        temp = inputList[i]
        inputList[i] = inputList[j]
        inputList[j] = temp
    return(inputList)

a = [4, 3, 2, 5]
print(sortSelection(a))