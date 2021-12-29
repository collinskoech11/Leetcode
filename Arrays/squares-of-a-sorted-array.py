
"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

"""
#Binary Search Solution
class Solution:
    def sortedSquares(self, nums):
        if len(nums) == 0:
            return []
        else:
            ans  = [0] * len(nums)
            l,r = 0, len(nums) - 1
            insertLoc = r
            
            while l <= r:
                lsq = nums[l] * nums[l]
                rsq = nums[r] * nums[r]
                
                if lsq <= rsq:
                    ans[insertLoc] = rsq
                    r -= 1
                    insertLoc -= 1
                else:
                    ans[insertLoc] = lsq
                    l+= 1
                    inserLoc -= 1
            return ans 
 #Arrays Soluttion 
class Soution:
    def sortedSquares(self, nums):
        ans = []
        if len(nums) == 0:
            return []
        for i in nums:
            ans.append(i*i)
        ans.sort()
        return ans
    
