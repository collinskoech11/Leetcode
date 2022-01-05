class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        target = 0
        if len(nums) <= 1:
            return []
        else:
            for i in range(len(nums)-2):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                target = 0-nums[i]
                L = i+1
                R = len(nums)-1
                while L<R:
                    sumNow = nums[L]+nums[R]
                    if sumNow < target:
                        L+=1
                    elif sumNow > target:
                        R-=1
                    else:
                        res.append([nums[i], nums[L], nums[R]])
                        while(L>R and nums[R-1] == nums[R]):
                            R-=1
                        L+=1
                        R-=1
            return res
