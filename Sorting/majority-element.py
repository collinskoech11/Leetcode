"""given an array nums return the element that appears the most number of times 
example nums = [1,2,2,2,3,2,2]
returns 2
"""
class Solution:
    def(self, nums:List[int]) -> int:
        c = Counter(nums)
        count = c.most_common(1)
        for v,k in count:
            return v
            
