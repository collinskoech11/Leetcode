"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

 

Constraints:

1) 1 <= nums.length <= 104
2)-104 < nums[i], target < 104
3) All the integers in nums are unique.
4) nums is sorted in ascending order.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int 
        """
        l,r = 0, len(nums) - 1 #left & right pointers
        while l <= r: #lpointer could be same as right pointer
            mid = l + (r - l)//2 #get the mid value using integer division
            if nums[mid] == target:
                return mid# target is at the mid value
            elif nums[mid] < target:# when target is greater than the mid val
                l = mid + 1# shift l pointer 1 index to the right of the mid value
            else:# target is less than the mid value
                r = mid - 1# shift r pointer 1 index to the left of the mid val
        return -1# if the target is not in the array
