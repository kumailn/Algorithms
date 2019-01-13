#Question: Add two binary numbers
#Solution: Recursively add the numbers based on the last digit
#Difficulty: Easy

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    #If one of the strings is null, return the non null one
    if not a or not b: return a or b
    #If both strings end with a 1, add a 0 at the end, let the 1 overflow into the addition of the two strings again
    if a[-1] == '1' and b[-1] == '1': return addBinary(addBinary(a[:-1], b[:-1]), '1') + '0' 
    #If both end in 0 simply add 0 at the end and continue the addition
    if a[-1] == '0' and b[-1] == '0': return addBinary(a[:-1], b[:-1]) + "0"
    #If one of them ends in 0 and the other doesn't, just add 1 to the end and add the rest of both strings
    return addBinary(a[:-1], b[:-1]) + '1'

def main():
    a = '1110'
    b = '1010'

    #Answer should be 11000
    print(addBinary(a, b))

main()