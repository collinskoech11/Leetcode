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
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
            elif letters[-1] <= target:
                return letters[0]
        
        
