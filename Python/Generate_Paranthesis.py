#Question: Generate all possible pairs of parenthesis for a given number n
#Solution: Recursive backtracking, keep count of left brackets and right brackets
#Difficulty: Medium 

def generateParenthesis(n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        def helper(results, string, leftCount, rightCount):
            #If we've reached the base case where no more brackets can be added, append the current string to our array
            if not leftCount and not rightCount: results += [string]
            #If there are still left brackers to be added, add left bracket and recall function with 1 less left bracket but 1 more right bracket (Since we've opened a new bracket that needs to be closed)
            if leftCount: helper(results, string + "(", leftCount-1, rightCount+1)
            #If there are right brackets that need to be added, add 1 then recall function with 1 less right bracket
            if rightCount: helper(results, string + ")", leftCount, rightCount-1)
        #Call initially with empty array, empty string, n left brackets and no right brackets
        helper(results, "", n, 0)
        return results