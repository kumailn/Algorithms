#Question: Find the difference between the bits of two numbers
#Solution: 

def hammingDistance(x, y):
        #Simply XOR the two numbers and count the hamming weight
        n, c = x ^ y, 0
        while n: 
            c += 1 if n & 1 else 0
            n >>= 1
        return c