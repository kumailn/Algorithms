# Question: Given a sudoku board, check if it is invalid
# Solution: Store each item in its correct row, col and block in a set or map, and check if it has been repeated
# Difficulty: Easy

def isValidSudoku(self, board: List[List[str]]) -> bool:
    alreadySeen = set()
    for i, row in enumerate(board):
        for j, number in enumerate(row):

            # We don't care if the number is empty
            if number == ".": continue
            
            # Store each of 3 categories in our set, for example if we come across a '5'
            # in the third row, first column and first block our set will contain {'5row3', '5col1', '5block1'}
            # this way if we ever run into a number that is in the same block/col/row it will already exist in our set
            # and we can look it up in O(1) time and return false if it does exist since it invalidates the sudoku board
            numberInRow = number + 'row' + str(i)
            numberInCol = number + 'col' + str(j)
            numberInBlock = number + 'block' + str(i//3) + str(j//3)
            
            if alreadySeen.intersection({numberInCol, numberInRow, numberInBlock}):
                return False
            
            alreadySeen.add(numberInCol)
            alreadySeen.add(numberInRow)
            alreadySeen.add(numberInBlock)
            
    return True 