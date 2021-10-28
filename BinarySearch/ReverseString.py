"""
Write a function that reverses a string. The input string is given as an array of characters s.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

"""

class Solution:
  def reverseString(self, s):
    #s.reverse() could also work
    l,r = 0, len(s) - 1
    
    while l < r:
      s[l], s[r] = s[r], s[l]
      l += 1
      r -= 1
