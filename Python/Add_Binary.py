#Add two binary numbers

#Trivial python solution
def addBinary(a, b):
    return (str(bin(int(a, 2) + int(b, 2)))[2:])