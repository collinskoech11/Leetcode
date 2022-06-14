"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set() # initialize set 
        l,res = 0, 0#left pointer and result counter
        for r in range(len(s)):#iterate through string s 
            while s[r] in seen:# if the current element is already oin set
                seen.remove(s[r])#remove the first element from the set
                l+=1# increment left pointer
            seen.add(s[r])# add the current element to the set
            res = max(res, r-l+1)# update result 
        return res
                
            
