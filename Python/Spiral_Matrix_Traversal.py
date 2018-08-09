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
  for i in range(len(matrix)):
    for j in range(len(matrix)):
      total += 1
      if(direction == 'R'):
        print(offset)
        if(j == (len(matrix) - 1 - offset)):
          traversal += ['X']
          direction = 'D'
        else:
          traversal += [matrix[i + offset][j - offset]]
      elif(direction == 'D'):
        traversal += [matrix[j][len(matrix) - 1 - offset]]
        if(j == (len(matrix) - 1 - offset)):
          traversal += ['X']
          direction = 'L'
      elif(direction == 'L'):
        traversal += [matrix[len(matrix) - 1 - offset][-1 * j - 1]]
        if(j == (len(matrix) - 1 - offset)):
          traversal += ['X']
          direction = 'U'
      elif(direction == 'U'):
        traversal += [matrix[-1 * j - 1][offset]]
        if(j == (len(matrix) - 1 - offset)):
          traversal += ['X']
          direction = 'R'
          offset += 1
  print(total)
  return traversal

print(spiral(test))