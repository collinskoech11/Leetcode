"""
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

 

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
"""

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        for i in range(len(words)-1):
            for j in range(i,(len(words))):
                print(i,j)
                wordl = words[i]
                wordr = words[j]
                pal = wordl + wordr
                if i != j:
                    if pal == pal[::-1]:
                        res.append([i,j])
                    pal2 = wordr + wordl
                    if pal2 == pal2[::-1]:
                        res.append([j,i])
        return res 