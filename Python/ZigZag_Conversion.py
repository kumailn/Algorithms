# Question: Given a string like "PAYPALISHIRING" produce a zigzag pattern like so
#           P     I    N
#           A   L S  I G
#           Y A   H R
#           P     I
# Solution: Create an array with elements equal to number of rows, keep a stepper to keep tack of 
#           wether to go up or down the zig-zag, flip the stepper everytime  
# Difficulty: Medium



def convert(s: str, numRows: int) -> str:
    if numRows == 1: return s
    
    i, step = 0, 1
    rows = [""] * numRows
    
    for letter in s:

        # For every letter we add it to some place in our array
        rows[i] += letter

        # We increment our pointer by the step, initially we simply increment it by 1
        # when we reach the bottom we reverse the step, and reverse again when get back to the top
        i += step

        # Reverse the step when we reach a upper or lower boundary
        if i == 0 or i == numRows - 1: step *= -1

    return "".join(rows)