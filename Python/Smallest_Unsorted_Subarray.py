


def smallesUnsortedSubarray(arr):
    i = -1
    while arr[i - 1] < arr[i]:
        i -= 1
    j = 0
    while arr[j] <= arr[i] and arr[j] <= arr[j + 1]:
        j += 1
    print(arr[j-1:i+1])



def main():
    a = [1, 4, 6, 8, 3, 2, 9]
    arr = [2,6,4,8,10,9,15]

    print(smallesUnsortedSubarray(a))
    print(smallesUnsortedSubarray(arr))

main()