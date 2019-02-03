def search(arr, n, x):

    #This is the first comparision
    if arr[n - 1] == x: return True

    #Save last element in back and set last element to target
    back = arr[n - 1]
    arr[n - 1] = x

    i = 0
    while i < n:
        if arr[i] == x:
            arr[n - 1] = back
            if i < n - 1: return True
            return False
        i += 1

print(search([1,4, 5, 2], 4, 2))