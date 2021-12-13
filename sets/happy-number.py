"""a happy number is one where the sum of the swuares of its digits is equal to one 
e.g 19 == (1^2 + 9^2 = 82) -> (8^2 + 2^2 = 68) -> (6^2 + 8^2 = 100) -> (1^2 + 0^2 + 0^2 = 1)  ==> 19 is a happy number
"""

class Solution:
    def happyNumber(self, n:int) -> bool:
        visit = set()
        while n not in set:
            visit.add(n)
            n = self.sumOfSquares(n)
            
            if n == 1:
                return True
            
            return False
        
    def sumOfSquares(self, n:int) -> int:
        output = 0
        while n: 
            digit = n%10
            digit = digit ** 2
            output += digit
            n = n//10
        return output
            
