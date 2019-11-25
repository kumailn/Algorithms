# Question (#394): Given an encoded string, return its decoded string.
# Solution: Use a stack and keep track of the last string you've built so far

def decodeString(s: str) -> str:
    # Contains the string we're adding to and the number we want to multiply the current string by
    stack = []
    num, string = 0, ''
    
    for char in s:
        # Every time we see an opening bracket, we know we need to start a new computation, so we push our current string and
        # the number we've seen so far to the stack and reset it 
        if char == '[':
            stack += [num, string]
            num, string = 0, ''
        # When we see a closing bracket we know something can be decoded, so we take the last string we had 
        # and add it to the current string * the number of times we want to expand it
        elif char == ']':
            string = stack.pop() + stack.pop() * string
        elif char.isdigit():
            num = num * 10 + int(char)
        else:
            string += char
        return string