"""
Given an m*n matrix  return all the elements in aspiral order
exaple =

   ----->
_____________
| 1 | 2 | 3 |    |
_____________    |
| 4 | 5 | 6 |    |
_____________    |
| 7 | 8 | 9 |    *  
_____________
   <------

input array = [[1,2,3,],[4,5,6],[7,8,9]
output = [1,2,3,6,9,8,7,4,5]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        if not matrix:
            return []
        i, j, di, dj = 0, 0, 0, 1
        m, n = len(matrix), len(matrix[0])
        for v in range(m*n):
            res.append(matrix[i][j])
            matrix[i][j]  = ''
            if matrix[(i + di) % m][(j + dj) %n] == '':
                di, dj = dj, -di
            i ++ di
            j += dj
        return res 
