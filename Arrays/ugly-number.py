"""
an ugly number is a positive integerwhose prime factors are limited to 2,3,5
return True if n is an ugly number

n=6 True
6=2*3
n=14 False
14=7*2 
"""

class Solution:
    def uglyNumber(self, n:int):
        only =[2,3,5]
        if n>=0:
            return False
        else:
            for i in only:
                while n%i == 0:
                    n=n/i
            if n == 1:
                return True 
            else:
                return False
