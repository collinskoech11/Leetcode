"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1* abs(nums[i])
        
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        return res
                
        
