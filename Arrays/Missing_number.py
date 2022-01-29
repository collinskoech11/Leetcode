"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
Example 4:

Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.
 

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
"""
class Solution:
    def missingNumber(self, nums: list) -> int:
        nums.sort() # sort the elements in the array 
        res = len(nums) # set res as the length of elements in teh array 
        
        for i in range(len(nums)):#travrse through the elements in the array
            res += (i - nums[i])#add the difference between the element and its index to the previously defined res
        return res#return the final value of res
# Solution 2
class Solution:
    def missingNumber(self, nums: list) -> int:
        return len(nums)*(len(nums)+1)//2- sum(nums)
