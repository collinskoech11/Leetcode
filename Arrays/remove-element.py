class Solution:
    def removeElement(self, nums:List[int], val: int) -> int:
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
            
        last, start = len(nums)-1, 0
        while start <= last:
            if nums[start] == val:
                if nums[last] == val:
                    last-=1
                else:
                    nums[start] = nums[last]
                    last -= 1
                    start += 1
            else:
                start += 1
        return start 

    
class Solutiontwo:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1:# check the length of the array
            if nums[0] == val:
                return 0# if first element = va return false
            else:
                return 1# return true
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count+=1
        return count
