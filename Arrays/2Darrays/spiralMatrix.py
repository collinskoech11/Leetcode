"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left,right = 0,len(matrix[0])# initialize pointers
        top,bottom = 0, len(matrix)# initialize pointers 
        while left < right and top < bottom:
            for i in range(left,right):#append the first row 
                res.append(matrix[top][i])
            top += 1 # increment top
            for j in range(top,bottom):# append the last column
                res.append(matrix[j][right-1])
            right-=1# decrement right
            if  not (left< right and top < bottom):# check if pointers have crossed each other
                break
            for k in range(right-1, left-1,-1):#append the bottom row in reverse order
                res.append(matrix[bottom-1][k])
            bottom -= 1# decrement bottom
            for k in range(bottom-1, top-1, -1):# append the first column in reverse order
                res.append(matrix[k][left])
            left+=1# increment left
        return res
            
