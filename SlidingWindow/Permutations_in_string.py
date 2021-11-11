"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

class Solution(object):
  def checkInclusion(self, s1,s2):
    if len(s1) > len(s2):
      return False
    
    length_of_s1 = len(s1)
    s1_counter = Counter(s1)
    window_counter = Counter()
    
    for 1, c in enumerate(s2):
      window_counter[c] += 1
      
      if i >= length_of_s1:
        element_from_left = s2[i -left_of_s1]
        
        if window_counter[element_from_left] == 1:
          del window_counter[element_from_left]
          
          else:
            window_counter[element_from_left] -= 1
            
        if window_counter == s1_counter:
          return True
        
     return False
