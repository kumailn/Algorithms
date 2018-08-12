tesft = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16]
]

test1 = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25]
]

test3 = [[2,5],[8,4],[0,-1]]

def spiral(matrix):
  directions = ["R", "D", "L", "U"]
  direction_index = 0
  direction = "R"
  traversal = []
  offset = 0
  total = 0
  x = 0
  y = 0
#   if(len(matrix) == 0):
#       return matrix
#   if(len(matrix) == 1):
#     for i in matrix:
#         traversal += [i]
#     return traversal
#   if(len(matrix[0]) == 1):
#     for i in matrix:
#         traversal += [i[0]]
#     return traversal
  if(len(matrix) == 0):
    return traversal
  for i in range(len(matrix) * len(matrix[0])):
    total += 1
    print(traversal, offset)
    if(direction == 'R'):
        traversal += [matrix[x][y]]
        if(y == (len(matrix[0]) - 1 - offset)):
            #traversal += ['X']
            direction = 'D'
            x += 1
        else:
            y += 1
    elif(direction == 'D'):
        traversal += [matrix[x][y]]
        if(x == (len(matrix) - 1 - offset)):
            #traversal += ['X']
            direction = 'L'
            y -= 1
        else:
            x += 1
    elif(direction == 'L'):
        traversal += [matrix[x][y]]
        if(y == offset):
            #traversal += ['X']
            direction = 'U'
            offset += 1
            x -= 1
        else:
            y -= 1
    elif(direction == 'U'):
        traversal += [matrix[x][y]]
        if(x == offset):
            #traversal += ['X']
            direction = 'R'
            y += 1
        else:
            x -= 1
  print(total)
  return traversal

print(spiral(test3))

