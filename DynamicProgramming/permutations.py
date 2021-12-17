"""
given an array of n distinct numbers return all possible permutations 
return the ans as a list of lists 
example :
nums = [1,2,3]
permutations = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
nums = [1]
permutations = [[1]]
"""



class Solution:
    def permute(self, nums:List[int]) -> List[List[int]]:
        result = []
        #base case
        if len(nums)==1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.append(perms)
            nums.append(n)
        return result
