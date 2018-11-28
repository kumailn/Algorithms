#Question: Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#Difficulty: Easy
def sortArrayByParity(A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[even], A[i] = A[i], A[even]
                even += 1
        return A