#Question: Given a string, reverse the positions of the words, for example 'hi my name is' becomes 'is name my hi'
#Solution: Reverse string, then reverse each word
#Time Complexity: O(n)

def reverseWords(strin):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """

        #Helper function to reverse items in a list from a start index to an end index
        def rev(start, end, stringList):
            #As long as the start index is less than the end index, swap the items at those indices and increment and decrement the indexs respectively 
            while start < end:
                stringList[start], stringList[end] = stringList[end], stringList[start]
                start += 1; end -= 1
            return stringList
        
        #Reverse the input string 
        strin[:] = strin[::-1]
        i = 0

        while i < len(strin):
            end = i
            #If the letter we're at is not a space, move up end to the next space
            if strin[i] != " ": 
                while end + 1 < len(strin) and strin[end] != " ": 
                    if strin[end + 1] == " ": break
                    end += 1
            #Reverse the string starting at index i to index end
            strin[:] = rev(i, end, strin)
            #Move i up to the next letter after the space
            i = end + 1
    
        return strin
        
def main():
    s = list("hi my name is")
    reverseWords(s)

    print(s)

main()