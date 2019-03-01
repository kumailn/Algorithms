#Question: Given a decoding for each letter in the alphabet (A-> 1, ... Z-> 26) determine the number of ways a given string of digits could be interpereted
#Solution: Recursively compute all possibilities using dynamic programming
#Difficulty: Medium

def numDecodings(s, l, store):

    #Set the index we're starting from to be the length of the string - the length we're at
    startIndex = len(s) - l

    #Recursive base cases -- If the length we're at is 0 return 1 (for 1 possibility)
    if(l == 0): return 1
    #If s starts with a 0 then it's invalid
    if(s[startIndex] == '0'): return 0
    #If we're already computed the possibilites at index l, return it
    if(store[l]): return store[l]
    
    #Recursively compute the number of decodings by subtracting 1 from the length 
    res = numDecodings(s, l - 1, store)

    #Recursively compute the number of decodings by subtracting 2 from the length and also cecking if those 2 numbers are <= 26 
    if(l >= 2 and int(s[startIndex] + s[startIndex + 1]) <= 26): res += numDecodings(s, l - 2, store)

    #Store the result in our dynamic programs array
    store[l] = res

    #Return the result
    return res  

def main():
    data = '12'
    print(numDecodings(data, len(data), [None] * (len(data) + 1)))
main()
