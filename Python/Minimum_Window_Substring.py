# Question: Given a string and a list of target letters, find the shortest continious string that has all those letters
# Solution/Pattern: The intuition here is to try and find the first substring that contains all letters and then try shrinking
#                   it's left boundary until we lose a character that was required. We contntinue to do this for all characters in 
#                   the string, hence creating a 'sliding window'
# Difficulty: Hard


def minWindow(self, s: str, t: str) -> str:

        # Initialize the starting point of our starting window
        start = 0
        shortest = len(s) + 1
        # We store the count of each letter needed in a hashmap 
        lookingFor = collections.Counter(t)
        # We also store the total number of chars we have left to find
        charsNeeded = len(t)
        shortestString = ""
        
        for end, v in enumerate(s):
            # If this char is one we were looking for (one that's present in our target) thenwe need 
            # to decrement it's count by one indicating we've seen it.
            # After we've decremented the count we need to check if we've seen it enough times, if the the 
            # count of the character is less than 0 that means that it's a extra char occuring more times than in t
            # However, if after decrementing we have a number greater than or equal to 0 then we can say this was one 
            # of the targets we were lookingFor and decrement our chars needed count  
            if v in lookingFor:
                lookingFor[v] -= 1
                if lookingFor[v] >= 0: charsNeeded -= 1

            # Now, if charsNeeded == 0, we can start shrinking our window from the left
            # since we don't need any more chars, we know the current string we have from start to end contains 
            # all the characters present in our target, so we can check if it's length is less than the the one we currently have
            # if it's length is less, we update the min length we've found so far and then update the shortest string we've found 
            # Every time we shrink the window we have to check if we're removing a character we actually needed and then update charsNeeded
            # if we removed a character that was required. Finally we shrink the window from the left by incrementing start
            while not charsNeeded:
                if shortest > end - start + 1:
                    shortest = end - start + 1
                    shortestString = s[start:end + 1]
                    
                if s[start] in lookingFor:
                    lookingFor[s[start]] += 1
                    if lookingFor[s[start]] > 0:
                        charsNeeded += 1
                start += 1
        return shortestString