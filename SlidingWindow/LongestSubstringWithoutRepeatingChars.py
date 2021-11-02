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
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""
class Solution(object):
  def lengthOfLongestSubstring(self, s):
    charSet = set()
    l=0
    res = 0
    
    for r in range(len(s)):
      while s[r] in charSet:
        charSet.remove(s[r])
        l += 1
      charSet.add(s[r])
      res = max(res, r - l + 1)
return res
