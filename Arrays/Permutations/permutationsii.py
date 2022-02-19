"""
Given a collection of numbers nums, that might contain duplicates return all ossible permutations in any order
Example 1:
Input: [1,1,2]
Output: [[1,1,2],[1,2,1],[2,1,1]]
Example 2:
Input: [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

""""
class Solution:
    def permuteUnique(elf, nums:List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = Counter(nums)
        def dfs():
            if len(perm) == len(perm):
                return
            for i in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    dfs()
                    count[n] += 1
                    perm.pop()
        dfs()
        return res
                    
                
                
