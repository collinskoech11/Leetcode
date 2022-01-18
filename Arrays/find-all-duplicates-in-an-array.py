"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
"""

#d.collections counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [elem for elem, count in Counter(nums).items() if count == 2]
   
   
   
   
   
   #solution using set 
   class Solution:
      def findDuplicates(self, nums: LIst[int]) -> List[int]:
        seen = set()
                seen_add = seen.add
                # adds all elements it doesn't know yet to seen and all other to seen_twice
                seen_twice = set( x for x in nums if x in seen or seen_add(x) )
                # turn the set into a list (as requested)
                return list( seen_twice )

