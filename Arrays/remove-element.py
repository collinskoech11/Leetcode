# Given an array and a value, remove all instances of that value in place and return the new length.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1:# check the length of the array
            if nums[0] == val:
                return 0# if first element = va return false
            else:
                return 1# return true
        
        last, start =  len(nums)-1, 0# Binary Search Pointers
        while start <= last:# while start is less than last
            if nums[start] == val:# check if element on start pointer is equal to val
                if nums[last] == val:# check if element on last pointer is equal to val
                    last -= 1# shift last pointer one step towards the start
                    print(nums,start)
                else:# while start is not less than last
                    nums[start] = nums[last]
                    last -= 1
                    start += 1
                    # print(nums,start)
            else:
                start += 1
                print(nums,start)
        return start
        print(nums,start)
        
