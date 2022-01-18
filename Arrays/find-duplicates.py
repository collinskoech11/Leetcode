"""Given an array of nums containing n+1 integers where each integer is in the range (i,n) inclusive of n 
There is one repeated element e=return the repeated element 


Space complexity should be O(1) - constant space.
Time complexity should be less than O(n^2).

"""
class Solution:
    def findDuplicate(self, nums:List[int]):
        six = set()
        for i in nums:
            if i not in six:
                six.add(i)
            else:
                return i
# Fast and slow pointer solution
class Solution:
    def findDuplicate(self, nums:List[int]):
        slow, fast = nums[0], nums[nums[0]]
        while fast != slow:
            fast, slow = nums[nums[fast]], nums[slow]
        fast = 0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow
