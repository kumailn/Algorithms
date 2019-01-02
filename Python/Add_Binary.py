#Add two binary numbers

#Trivial python solution
def addBinary(a, b):
    return (str(bin(int(a, 2) + int(b, 2)))[2:])

def addBinary(a, b):
    if not a or not b: return a or b
    if a[-1] == '1' and b[-1] == '1': return addBinary(addBinary(a[:-1], b[:-1]), '1') + '0' 
    if a[-1] == '0' and b[-1] == '0': return addBinary(a[:-1], b[:-1]) + "0"
    return addBinary(a[:-1], b[:-1]) + '1'