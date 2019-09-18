# Question: Given a string, find the first character that is unique
# Solution: Count the occurance of each letter, find the first letter with 1 occurance from your hashmap
#           because we don't want to loop over our input string twice if it's very long
# Difficulty: Easy

def firstUniqChar(s: str) -> int:
        # Create a hashmap to store the counts of each letter as well as the index
        letterCounts = {}

        # Store the lowest index we see with a letter count of 1 when we traverse our hashmap
        smallestIndex = len(s)

        # Store each items count as well as the first index it occured at
        for i, v in enumerate(s):
            getChar = letterCounts.get(v, [0, i])
            letterCounts[v] = (getChar[0] + 1, getChar[1])

        # Loop through the hashmap updating the smallestIndex each time we see a letter
        # with a count of 1 and a smaller index than the previous 
        for i, v in enumerate(letterCounts):
            if letterCounts[v][0] == 1:
                smallestIndex = min(smallestIndex, letterCounts[v][1])
                        
        # Return either the index of the first char or -1 if there is no unique char
        return smallestIndex if smallestIndex != len(s) else -1
