# Question: Given a matrix (2x2 array), traverse it in a spiral
# # Solution: Track the offset of the inner level of the spiral we're at, keep track of the directions 
# Difficulty: Medium

def spiralOrder(matrix):

    # Initially our direction needs to be right and our offset 0
    direction = "R"
    i = j = offset = 0
    result = []
    if not matrix: return matrix
    m, n = len(matrix) - 1, len(matrix[0]) - 1
    
    # Loop through the number of values in the matrix
    for _ in range(len(matrix) * len(matrix[0])):
        result += [matrix[i][j]]

        # If the direction is right keep incrementing j (the horizantal index)
        # once j reaches the end (the length of the horizantal - the offset), switch directions 
        # accordingly; similar approaches for when traversing down and left
        if direction == "R": 
            if j == n - offset: direction = "D"  
            else: j += 1
        if direction == "D": 
            if i == m - offset: direction = "L"  
            else: i += 1
        if direction == "L": 
            if j == offset: direction = "U"  
            else: j -= 1

        # If we're traversing upwards we need to increment the offset once i is 1 more than the offset,
        # this is because if i == offset + 1 then i is right below the offset and we want to start traversing
        # an inner spiral of the matrix. We also increment j in this case and indicate the next move is to the right 
        if direction == 'U': 
            if i == offset + 1: 
                direction = "R"
                offset += 1
                j += 1
            else: i -= 1
            
    return result

