#Question: Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
#Solution: Remove all non letter chars and then reverse string, then traverse original string inserting non letter chars back into original indexes
#Time Complexity: O(n)

def reverseOnlyLetters(S):
        """
        :type S: str
        :rtype: str
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        #Construct a new list consisting of ONLY the letters in S and reverse it
        s2 = [letter for letter in S if letter in alphabet][::-1]
                
        #Loop through S and insert non letters into s2 
        for i, letter in enumerate(S):
            if letter not in alphabet: s2.insert(i, letter)
            
        return ''.join(s2)
        
        
def main():

    #Should be "Qedo1ct-eeLg=ntse-T!"
    print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))

main()