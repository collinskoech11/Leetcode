"""
# represents a backspace in a string such that 
 s = "ab#c", t = "ad#c"
 s = "ac", t = "ac"  => true 
 return true if s and t are equal after getting rid of the backspace
"""

class Solution:
    def backspaceStringCompare(self, S: str, T:str) -> bool:
        SS = []
        TT = []
        for i in S:
            if i == "#":
                if len(SS) >= 1:
                    SS.pop()
            else:
                SS.append(i)
        for i in T:
            if i == "#":
                if len(TT) >= 1:
                    TT.pop()
            else:
                TT.append(i)
                
        return SS == TT 
           
