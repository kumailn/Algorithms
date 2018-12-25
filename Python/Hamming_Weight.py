#Question: Find the number of 1s in the binary representation of a number
#Solution: Keep counting last bit and bitshifting by 1
#Difficulty: Easy

def hammingWeight(self, n):
        #Variable to count the weight
        c = 0
        #While number is not null (ie 0)
        while n:
            #Increment c by 1 if last bit of number is 1 (Check last bit by doing bitwise AND with 1)
            c += 1 if n & 1 else 0
            #Right shift number by 1 bit (essentially, delete rightmost bit)
            n >>= 1
        return c