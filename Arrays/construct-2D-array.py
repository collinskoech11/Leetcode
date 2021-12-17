"""
given a non empty one dimensional array and two integers m and n  construct a 2D array m rows and n columns 
return an m*n 2dimensional array
[1,2,3,4]
m = 2
n = 2
return [[1,2],[3,4]]
"""
class Solution:
    def construct2DaArray(self, original:List[int], n:int, m:int):
        total = len(original)
        if m*n !=total:
            return []
        answer = []
        itr = 0
        
        for iterations in range(1, n+1):
            arr = []
            while itr < iterations*n:
                arr.append(original[itr])
                itr += 1
            answer.append(arr)
        return answer
