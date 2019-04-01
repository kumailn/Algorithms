def minWindow(s: str, t: str) -> str:
    
    #Trivial base case
    if not s or not t: return ""
    
    #Initialize a hashmap with the count of each character in t        
    _map = {t[i]:t.count(t[i]) for i in range(len(t))}
    
    #Declare minlen to be ∞
    minlen = float('inf')
            
    #initialize letterCount, localLeft and globalLeft to 0
    letterCount = localLeft = globalLeft = 0
    
    #For every letter in s
    for i, current in enumerate(s):
        
        #If the letter is in the map, subtract 1 from it and increment letterCount if its count is >= 0
        if current in _map: 
            _map[current] -= 1
            if _map[current] >= 0: letterCount += 1
                
        #While our letterCount is the same as the len of t
        #Note this block of code will only execute when we've found a substring with all letters in t
        while letterCount == len(t):
            
            #If our (current index - localLeft + 1) is less than minlen
            #In other words if the length of the substring we've localLeftust found is less than the minimum one we know, we'll update minlen and globalLeft
            #Note localLeft denotes the leftmost index of our candidate substring and minlen denotes the global leftmost index that results in the shortest substring
            if i - localLeft + 1 < minlen: globalLeft, minlen = localLeft, i - localLeft + 1
            
            #If the leftmost item is in the map, add 1 to it and decrement letterCount if its still > 0
            #This essentially means we now need to look for this letter again since we're shifting an index that includes a letter we want
            #We decrement letter count if its value in the map is non-zero to signify we're missing a letter, since letterCount is no longer the same length as t, we also exit the while loop now
            if s[localLeft] in _map:
                _map[s[localLeft]] += 1
                if _map[s[localLeft]] > 0: letterCount -= 1
            
            #Keep shifting the localLeft pointer right to find smaller and smaller windows
            localLeft += 1
        
    if minlen > len(s): return ""                    
    return s[globalLeft:globalLeft+minlen]
            
def main():
    print(minWindow('ADOBECODEBANC', 'ABC'))

main()