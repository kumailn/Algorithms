#Question: Find the difference between the bits of two numbers
#Solution: XOR the two numbers (Creates a new number with 1s in place of the differences), then find hamming weight (See Hamming_Weight.py)
#Difficulty: Easy

def hammingDistance(x, y):
        #Simply XOR the two numbers and count the hamming weight
        n, c = x ^ y, 0
        while n: 
            c += 1 if n & 1 else 0
            n >>= 1
        return c