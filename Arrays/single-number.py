"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                del counts[n]
                
        return  list(counts.keys())[0]
       
       
# OPtimal solution

c = Counter(nums)
for n  in c:
   if c[n] == 1:
      return n 

#sample soln 

return 2*sum(set(nums)) - sum(nums)
        
