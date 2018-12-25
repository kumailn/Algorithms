#Question: Given a number, find all the possible combinations you could make with it using a traditional cellphone keyboard
#Solution: Use backtracking

def letterCombinations(digits):
        digits = str(digits)
        #Keep track of all the possible comibnations we can make
        possibleCombinations = []
        #If we have no number, return our list
        if not digits: return possibleCombinations
        #Define a dictionary that maps a number to the letters on the keypad
        keypad = {1: " ", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        #Define a recursive helper that backtracks to find possible combinations
        def r(digitsString, currentResultString):
            #If we've reached a digit string of null, we can append our constructed result to our result list
            if not digitsString: possibleCombinations.append(currentResultString)
            else: 
                #For every letter in the possible letters of the first letter of the digitstring
                for i in keypad[int(digitsString[0])]:
                    #Recall the recursive helper on the digitstring but without the first number, and the result string but with the mapped letter
                    r(digitsString[1:], currentResultString + (i if i != " " else ""))
        #Run our helper initially on the original number, and an empry result string
        r(digits, "")
        return possibleCombinations

def main():
    print(letterCombinations(321))

main()