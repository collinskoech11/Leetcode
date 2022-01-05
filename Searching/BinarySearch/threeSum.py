"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        target = 0
        if len(nums) <= 1:# Base case
            return []
        else:
            for i in range(len(nums)-2):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                target = 0-nums[i]
                L = i+1
                R = len(nums)-1
                while L<R:
                    sumNow = nums[L]+nums[R]
                    if sumNow < target:
                        L+=1
                    elif sumNow > target:
                        R-=1
                    else:
                        res.append([nums[i], nums[L], nums[R]])
                        while(L>R and nums[R-1] == nums[R]):
                            R-=1
                        L+=1
                        R-=1
            return res
