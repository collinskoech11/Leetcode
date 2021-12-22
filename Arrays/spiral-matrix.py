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
