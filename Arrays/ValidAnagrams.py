"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !== len(t): # check lengths of both strings
            return False # valid anagrams have equal lengths
         
        scounter = {}# create a dictionary for both
        tcounter = {}
        for i in s:
            if i not in scounter:
                scounter[i] = 1#initialize counter as one if not already in dictionary
            else:
                scounter[i] += 1# increment value if element is already present
        for j in t:
            if j not in tcounter:
                tcounter[j] = 1
            else:
                tcounter[j] += 1
        print(scounter, tcounter)
        for r in scounter:
            if r in tcounter:
                if scounter[r] != tcounter[r]: # compare valur in sCounter and value in tCounter
                    return False
            else: 
                return False
        for x in tcounter:
            if x in scounter:
                if tcounter[x] != scounter[x]: # compare valur in sCounter and value in tCounter
                    return False
            else:
                return False
        return True # return True if loop completes
        
            
