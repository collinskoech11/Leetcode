"""Given an array of nums containing n+1 integers where each integer is in the range (i,n) inclusive of n 
There is one repeated element e=return the repeated element 


Time complexity
O(n) travesing through all elements in the array 
Space complexity

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
