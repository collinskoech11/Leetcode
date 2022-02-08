class Solution:
    # solution using a single for loop O(N) runtime O(1) space complexity -> we only allocate space for res once 
    def missingNUmber(self, nums:List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res
# [3,0,1] res = 3
# 1st iteration -> res = (0)
# i = 0 
# res =  i-nums[i] + res  => 0-3 +3 = 0
# 2nd iteration -> res = (1)
# i = 1 
# res = i-nums[i] + res => 1-0 +0 = 1
# 3rd iteration -> res = (2)
# i = 2 
# res = i-nums[i] + res => 2-1 + 1 = 2

class Solution:
    def missingNumber(self, nums:List[int]) -> int:
        return (((len(nums))*(len(nums)+1))//2) -sum(nums)
