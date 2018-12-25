#Question: Given a string, find the longest palindrome in it
#Difficulty: Iterate through each element and determine if its a palindrome
#Difficulty: Easy

def longestPalindrome(s):
        #Keep track of largest palindrome found so far
        gmax = ""
        #Helper function to find the longest palindrome given a left starting index and a right starting index 
        def checkPal(s, l, r):
            #As long as l >= 0 and r is less than length of the string and the items at s and l are equal
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            #Return s[l+1:r] because the while loop will exit after it is done one extra decrement of l, (ie s[l] != s[r] anymore), and up to r because python list slicing goes up to but not including 
            return s[l + 1: r]
        #For each index in s
        for i in range(len(s)):
            #Check the palindrome as an odd palindrome, so where both l and r are equal, and as an even length palindrome
            o, e = checkPal(s, i, i), checkPal(s, i, i + 1)
            #Set gmax to the longest palindrome found
            if len(o) > len(gmax): gmax = o
            if len(e) > len(gmax): gmax = e
        return gmax