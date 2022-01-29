class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Sample Brute Force Spolution
        # Runtime -> O(N^3) N for creating the set, check length nums, check len seen .
        seen = set(nums)
        if len(nums) > len(seen):# Sample Brute Force Spolution
            return True
        else:
            return False
          # Runtime -> O(N^2) N for iterating through each of the elemens in muns ,append to xseen .
        xseen = set()
        for i in nums:
            if i in xseen:
                return True
            else:
                xseen.add(i)
        return  False
