class Solution:
    def sortColors(self, nums: list[int]) -> None:

        count = Counter(nums)

        for i in range(len(nums)):
            if count[0]> 0:
                nums[i] = 0
                count[0] -= 1
            elif count[1] > 0:
                nums[i] = 1
                count[1] -= 1
            else:
                nums[i] = 2