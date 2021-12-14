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
