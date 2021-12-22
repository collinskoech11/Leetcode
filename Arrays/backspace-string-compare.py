"""
# represents a backspace in a string such that 
 s = "ab#c", t = "ad#c"
 s = "ac", t = "ac"  => true 
 return true if s and t are equal after getting rid of the backspace
"""

class Solution:
    def backspaceStringCompare(self, S: str, T:str) -> bool:
        SS = []# create an empty array for s
        TT = []# create an empty array for t
        for i in S:#for any element in s
            if i == "#":#if the current element is #
                if len(SS) >= 1:
                    SS.pop()#pop the last edded element from the created array if ts length is greater than one
            else:
                SS.append(i)#if element at i isn't # apend it to the array
        for i in T:#for any element in t
            if i == "#":#if the current element is #
                if len(TT) >= 1:
                    TT.pop()#pop the last edded element from the created array if ts length is greater than one
            else:
                TT.append(i)#if element at i isn't # apend it to the array
                
        return SS == TT #return true if the two created arrays are the same
           
