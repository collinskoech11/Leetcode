"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively."""

class Solution:
    def sortColors(self, nums: list[int]) -> None:

        count = Counter(nums)

        for i in range(len(nums)):
            if count[0]> 0:
                nums[i] = 0
                count[0] -= 1
            elif count[1] > 0:
                nums[i] = 1
                count[1] -= 1
            else:
                nums[i] = 2
