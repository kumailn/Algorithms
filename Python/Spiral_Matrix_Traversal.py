test = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16]
]

def spiral(matrix):
  directions = ["R", "D", "L", "U"]
  direction_index = 0
  direction = "R"
  traversal = []
  offset = 0
  total = 0
  x = 0
  y = 0
  for i in range(len(matrix) * len(matrix)):
    print("Off", offset, traversal)
    total += 1
    if(direction == 'R'):
        traversal += [matrix[x][y]]
        if(y == (len(matrix) - 1 - offset)):
            print("Item", matrix[x][y])
            #traversal += ['X']
            direction = 'D'
            x += 1
        else:
            y += 1
        print("x and y", x,y)
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
  return traversal

print(spiral(test))
