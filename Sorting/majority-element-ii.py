"""given an array nums return the elements that appears n/3 or more times
example nums = [3,2,3]
returns [3]"""

class Solution:
    def majorityElement(self, nums:List[int]) -> List[int]:
        return [elem for elem, count in Counter(nums).items() if count > len(nums)/3]
