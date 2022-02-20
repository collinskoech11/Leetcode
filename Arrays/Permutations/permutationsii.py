"""
Given a collection of numbers nums, that might contain duplicates return all possible permutations in any order
Example 1:
Input: [1,1,2]
Output: [[1,1,2],[1,2,1],[2,1,1]]
Example 2:
Input: [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

""""
class Solution:
    def permuteUnique(elf, nums:List[int]) -> List[List[int]]:
        res = []# store the list of all permutations 
        perm = []# store each urrent permutation 
        count = Counter(nums)# use counter to check for duplicates from d.collections 
        # || { n:0 for n in nums } set n to zero for each unique element in nums
        # for n in nums: count[n] += 1 for every element update its count by one
        def dfs():# Backtracking fx
            if len(perm) == len(nums):# Base case if the permutation is complete and we dont have any number to add
                res.append(perm.copy())# 
                return
            for i in count:#brute force => choose every choice that we can / go through every number in count (every key is unique
                if count[n] > 0:# make sure count is greater than 0 meaning that we are alowed to choose it
                    perm.append(n)# append the current n to the permutration
                    count[n] -= 1# decrement the current count by one
                    dfs()# call the dfs() fx at this point we have gotten to the base case
                    count[n] += 1
                    perm.pop()
        dfs()
        return res
                    
                
                
