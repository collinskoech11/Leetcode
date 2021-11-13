class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        a = {}
        for i in range(len(nums)):
            current = nums[i]
            if current in a and k>=1-a[current]:
                return True
            else:
                a[current]=i
        return False
                
