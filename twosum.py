class Solution(object):
    def twoSum(self, nums, target):
        seen={}

        for index, num in enumerate(nums):
            other = target - num

            if other in seen :
                return[seen[other],index]
        return[]
        """ 
        :type nums: list[int]
        :type target: int
        :type: List[int]
        """