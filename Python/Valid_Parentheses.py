# Question: Given a string of parentheses determine if it's valid or not
# Solution: Keep a stack of seen opening parentheses 
# Difficulty: Easy

def isValid(s: str) -> bool:
        pairs = {'(':')', '{':'}', '[':']'}
        stack = []

        for i, v in enumerate(s):

            # Add to the top of the stack if it's a opening bracket
            if v in '({[': stack += [v]

            # If the stack is not empty and the top is the pair of the current closing bracket, pop it
            elif stack and pairs[stack[-1]] == v: del stack[-1]

            # If the stack became empty at any point ot the brackets didnt match, return False
            else: return False

        # Return true if the stack is empty
        return not stack
                