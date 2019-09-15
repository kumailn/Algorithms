# Question: (#161) Given two strings s and t, determine if they are both one edit distance apart.
# Solution: Use two pointers and a variable to keep track of the edits. Shift the pointer of the longer string 
#           when we see characters which aren't the same and count that edit.
# Difficulty: Medium 

def isOneEditDistance(self, s: str, t: str) -> bool:
    # Since the strings need to be exactly 1 edit apart, if they're the same
    # of if they differ in length by more than one, we know they arent one edit apart
    if s == t or abs(len(s) - len(t)) > 1: return False
    if len(t) > len(s): s, t = t, s
    i = j = edits = 0
    
    while i < len(s) and j < len(t):

        # When we run into a character that's not the same in 
        # both strings, increment the pointer of the longer string or
        # if both strings have the same length, increment both pointers.
        if s[i] != t[j]:
            edits += 1
            i += 1
            if len(s) == len(t): j += 1

        # If they character was the same just increment both pointers 
        else: i += 1; j += 1

        # If ever edits becomes more than one we can return false
        if edits > 1: return False
    return True