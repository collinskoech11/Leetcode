class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        start = 0
        last = len(nums)-1
        result = 0
        while start <= last:
            if nums[start] == val:
                if nums[last] == val:
                    last -= 1
                else:
                    nums[start] = nums[last]
                    last -= 1
                    start += 1
            else:
                start += 1
        return start
        
