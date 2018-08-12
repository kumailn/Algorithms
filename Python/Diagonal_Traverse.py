inp = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

def diagonal(matrix):
    direction = "R"
    traversal = []
    x = y = 0
    for i in range(len(matrix[0]) * len(matrix)):
        if(direction == "R"):
            traversal += [matrix[x][y]] 
            y += 1
        
