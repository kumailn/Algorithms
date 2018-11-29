#Question: Given a sudoku board, check if it is invalid
#Solution: Store each item in its correct row, col and block in a map, and check if it has been repeated
#Difficulty: Easy

def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = {}
        for i, v in enumerate(board):
            for j, w in enumerate(v):
                if w == ".": continue 
                if (w + "row" + str(i)) in seen: return False
                if (w + "col" + str(j)) in seen: return False
                if (w + "block" + str(i//3) + str(j//3)) in seen: return False
                
                seen[w + "row" + str(i)] = True; seen[w + "col" + str(j)] = True; seen[w + "block" + str(i//3) + str(j//3)] = True
        return True
                