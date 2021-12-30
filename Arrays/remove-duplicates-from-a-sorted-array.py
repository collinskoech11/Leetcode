class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pre = 0
        for cur in range(1,len(nums)):
            if nums[cur]!=nums[pre]:
                pre+=1
                nums[pre]=nums[cur]

        return pre+1
