#Basically a modified Kadanes algorithm
def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        #Trivial case
        if not s: return 0
        #Let global max and global min the first item
        cmax, gmax = [s[0]], [s[0]]
        #For i in range from the second element to last
        for i in range(1, len(s)):
            #If element is not in the current max, then append
            if s[i] not in cmax: cmax += [s[i]]
            #Otherwise, delete everything in current max up to the current element, and append the current element
            else: 
                cmax = cmax[cmax.index(s[i]) + 1:] + [s[i]]
            #If current max is greater than global max, set global to current
            if len(cmax) > len(gmax): gmax = cmax
        return len(gmax)


#More compact
def lengthOfLongestSubstring2(s):
        """
        :type s: str
        :rtype: int
        """
        cmax = gmax = [s[0]] if s else []
        for i in range(1, len(s)):
            cmax = cmax + [s[i]] if s[i] not in cmax else cmax[cmax.index(s[i]) + 1:] + [s[i]]
            if len(cmax) > len(gmax): gmax = cmax
        return len(gmax)