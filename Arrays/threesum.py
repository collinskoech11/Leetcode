'''
Leetcode: 3Sum
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ? b ? c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},
    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
http://leetcode.com/2010/04/finding-all-unique-triplets-that-sums.html
O(logn)
'''

class Solution:    
    def three_sum(nums):
        nums = sorted(s) # O(nlogn)
        output = set()
        for k in range(len(nums)):
            target = -s[k]
            i,j = k+1, len(nums)-1
            while i < j:
                sum_two = nums[i] + nums[j]
                if sum_two < target:
                    i += 1
                elif sum_two > target:
                    j -= 1
                else:
                    output.add((nums[k],nums[i],nums[j]))
                    i += 1
                    j -= 1
        return output
