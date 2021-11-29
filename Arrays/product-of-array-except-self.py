"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer."""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """right_multiply = [0] * len(nums)
        right_multiply[-1] = nums[-1]
        for i in range(1, len(nums)):
            right_multiply[len(nums)-i-1] = right_multiply[len(nums)-i] * nums[len(nums) - i - 1]
            
        output = [0]*len(nums)
        prefix = 1
        current_index = 0
        while current_index < len(output) -1:
            output[current_index] = prefix * right_multiply[current_index+1]
            prefix *= nums[current_index]
            current_index+=1
        output[-1] = prefix
        return output"""
        output = [1 for i in range(len(nums))]
        for i in range(1,len(output)):
            output[i] = output[i-1]*nums[i-1]
        R = 1
        for i in range(len(output)-1, -1, -1):
            output[i] = output[i]*R
            R *=nums[i]
        return output
        
