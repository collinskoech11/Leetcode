"""
Given an array nums of diztinct integers, return all the possible permutations. you can return the answer in order.
example 1: nums = [1,2,3]
Output: [[1,2,3],[1,2,3],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
example 1: nums = [0,1]
Output: [[0,1],[1,0]]
example 1: nums = [1]
Output: [[1]] Base case (No computation happens )
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result  = []
        if len(nums) == 1:# base case 
            return [nums[:]]# return nums but as a list of lists 
        for i in range(len(nums)):
            n = nums.pop(0)# remove the first element 
            perms = self.permute(nums)# get the different possible arrangements of the remaining part of the array 
            
            for perm in perms:#for each permutation
                perm.append(n)# append the previously popped element 
            result.extend(perms)# extend function appends different arrays to one [].extend(perms) perms = [1,2,3] [2,3,1] => [[1,2,3],[2,3,1]]
            nums.append(n)# append the previously popped element 
        # result.sort() # sort the List of lists  OPTIONAL STEP SINCE THE QN ALLOWS YOU TO RETURNN THE RESULT IN ANY ORDER
        return result   
