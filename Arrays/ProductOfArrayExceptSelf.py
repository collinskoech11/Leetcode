
'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''


class Solution:
    def productExceptSelf(self, nums:List[int]) -> List[int]:
        res = [1]*(len(nums))#initialize res array with length of nums 
        prefix = 1
        
        for i in range(len(nums)):
            res[i] *= prefix# initialize element of res as current prefix
            prefix *= nums[i]# update prefix by multiplying it with the num at the current index
        postfix = 1# initialize postfix as one 
        for i  in range(len(nums)-1, -1,-1,-1):# iterate through the array nums in reverse order
            res[i] *= postfix# update res by multiplying current index with postfix
            postfix *= nums[i]# update the posfix value 
        return res
