"""
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Example 3:

Input: letters = ["c","f","j"], target = "d"
Output: "f"
Example 4:

Input: letters = ["c","f","j"], target = "g"
Output: "j"
Example 5:

Input: letters = ["c","f","j"], target = "j"
Output: "c"
"""
class Solution:
  def nextGratestLetters(self, letters: List[str], tartget: str) -> str:
    l,r = 0, len(letters) - 1
    while l < r:
      mid = (r-l)//2 + 1
      if letters[mid] <= target:
        l = mid + 1
      else:
        r = mid
        
   return letters[l%len(letters)]
