# given a n*n 2D matrix representing an image rotate the image by 90 deg (clockwise)
# rotation in place (do not allocate another 2d matrix for the rotation 
# example 1
# input matrix = [[1,2,3],[4,5,6],[7,8,9]]
# output = [[7,4,1],[8,5,2],[9,6,3]]

#example 2
# input matrix = [[1]]
# output = [[1]]

class Solution:
    def rotate(self, matrix:list[List[int]]) -> None:
        n = len(matrix[0])
        for row in range(n):
            for col in range(row,n):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
                
        for i in range(n):
            matrix[i].reverse()
