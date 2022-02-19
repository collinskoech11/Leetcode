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
        res = []# store the list of all permutations 
        perm = []# store each urrent permutation 
        count = Counter(nums)# use counter to check for duplicates 
        def dfs():# Backtracking fx
            if len(perm) == len(perm):# Base case 
                res.append(perm.copy())
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
                    
                
                
