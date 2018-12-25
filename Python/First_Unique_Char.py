#Question: Given a string, find the first character that is unique
#Solution: Count the occurance of each letter, find the first letter with 1 occurance
#Difficulty: Easy

#Complexity: Time O(2n) - Space O(n)
def firstUniqChar(s):
        #Create a hashmap (dictionary) to store the counts of each letter
        d = {}
        #For each item in the string, store it in the map, and count its occrance
        for i in s:
            if i in d: d[i] += 1
            else: d[i] = 1
        #Loop through string again, if the current letters count is 1 return that letter
        for i, v in enumerate(s):
            if d[v] == 1: return i
        return -1