"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
"""
class Solution:
    # solution using a single for loop O(N) runtime O(1) space complexity -> we only allocate space for res once 
    def missingNUmber(self, nums:List[int]) -> int:
        res = len(nums)#initialize res to the lenth of the array
        for i in range(len(nums)):#traverse through the entire array
            res += i - nums[i]# sum the difference of the index to and the value in nums sat that index
        return res
# [3,0,1] res = 3
# 1st iteration -> res = (0)
# i = 0 
# res =  i-nums[i] + res  => 0-3 +3 = 0
# 2nd iteration -> res = (1)
# i = 1 
# res = i-nums[i] + res => 1-0 +0 = 1
# 3rd iteration -> res = (2)
# i = 2 
# res = i-nums[i] + res => 2-1 + 1 = 2

class Solution:
    def missingNumber(self, nums:List[int]) -> int:
        return (((len(nums))*(len(nums)+1))//2) -sum(nums)
