class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []# initialize an empty array to append all subsets
        subset = []# for each possible subset
        def dfs(i):#Initialize Depth first search to get all  subsets 
            if i >= len(nums):
                res.append(subset.copy())
                return
            print(i)
            # descision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            
            # decision not to include nums[i]
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return res