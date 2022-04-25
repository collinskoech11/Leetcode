"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

class Solution:
    def validSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        # check rows
        for i in range(len(board)-1):
            for j in range(len(board[i])-1):
                if board[i][j] not in seen:
                    seen.add(board[i][j])
                else: 
                    return False
            seen.clear()
        #check columns
        for x in range(len(board)-1):
            for y in range(len(board[x])-1):
                if board[y][x] not in seen:
                    seen.add(board[y][x])
                else:
                    return False
            seen.clear()
        # check 3x3 grids 
        for r in range(len(board)-1):
            for c in range(len(board[r])):
                if r <= 2:
                    if board[r][c] not in seen:
                        seen.add(board[r][c])
                    else:
                        return False
                seen.clear()
                if r > 2 and r <= 5:
                    if board[r][c] not in seen:
                        seen.add(board[r][c])
                    else:
                        return False
                seen.clear()
                if r > 5 and r <= 8:
                    if board[r][c] not in seen:
                        seen.add(board[r][c])
                    else:
                        return False
                seen.clear()
        return True
        
