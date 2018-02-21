#Insertion sort implementation in Python
def sortInsert(inputList):
    index = 1
    for i in range(1, len(inputList)):
        while(inputList[i] < inputList[i - 1]):
            print("Iteration: ", a)
            temp = inputList[i]
            inputList[i] = inputList[i - 1]
            inputList[i-1] = temp
            i = i - 1
    return inputList

a = [1, 7, 5, 4, 3, 2]
sortInsert(a)
print(a)
