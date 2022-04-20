'''
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
'''

class Solution:
  def smallestMissingPositive(self, nums:List[int]) -> int:
    nset = set(nums) # create a set containing all non repeated elements of nums
    i = 1 # initialize i as the smallest expected missing positiv integer
    while i in nset:
      i+=1 # if i is already in nset increment i by one and repeat the process until the current value of i is not found in the set
    return i# return i as the smallest missing positive integer
    
