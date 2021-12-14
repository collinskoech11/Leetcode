"""return the nth ugly number
[1,2,3,4,5,6,8,9,10,12]
                     ^
                     |
                     nth ugly number
        ^            
        |
        n = 10
        length of the array containing the ugly numbers
        
        
the function returns the nth ugly number
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        two = three = five = 0
        while len(ugly) < n:
            while ugly[two]*2 <= ugly[-1]:
                two += 1
            while ugly[three]*3 <= ugly[-1]:
                three+=1
            while ugly[five]*5 <= ugly[-1]:
                five+=1
            ugly.append(min(ugly[two]*2, ugly[three]*3, ugly[five]*5))
            
        return ugly[-1]
    
    
