#Binary Search Solution
class Solution:
    def sortedSquares(self, nums):
        if len(nums) == 0:
            return []
        else:
            ans  = [0] * len(nums)
            l,r = 0, len(nums) - 1
            insertLoc = r
            
            while l <= r:
                lsq = nums[l] * nums[l]
                rsq = nums[r] * nums[r]
                
                if lsq <= rsq:
                    ans[insertLoc] = rsq
                    r -= 1
                    insertLoc -= 1
                else:
                    ans[insertLoc] = lsq
                    l+= 1
                    inserLoc -= 1
            return ans 
 #Arrays Soluttion 
class Soution:
    def sortedSquares(self, nums):
        ans = []
        if len(nums) == 0:
            return []
        for i in nums:
            ans.append(i*i)
        ans.sort()
        return ans
    
