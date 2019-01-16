#Question: Given a string, find the first character that is unique
#Solution: Count the occurance of each letter, find the first letter with 1 occurance
#Difficulty: Easy

#Complexity: Time O(2n) - Space O(n)
def firstUniqChar(s):

        #Create a hashmap (dictionary) to store the counts of each letter
        letterCounts = {}

        #For each item in the string, store it in the map, and count its occrance
        for letter in s:
            if letter in letterCounts:
                letterCounts[letter] += 1
            else:
                letterCounts[letter] = 1

        #Loop through string again, if the current letters count is 1 return that letter
        for i, v in enumerate(s):
            if letterCounts[v] == 1: return i
                
        return -1

def main():
    print(firstUniqChar('kayak'))

main()