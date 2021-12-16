"""
an ugly number is a positive integer whose prime factors are imited to 2,3,5
return the nth ugly number
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
while len(ugly) < n:
            while ugly[two]*2 <= ugly[-1]:
                two += 1
            while ugly[three]*3 <= ugly[-1]:
                three+=1
            while ugly[five]*5 <= ugly[-1]:
                five+=1
            ugly.append(min(ugly[two]*2, ugly[three]*3, ugly[five]*5))
"""class Solution:
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
            
        return ugly[-1]"""
class Solution:
    def nthUglyNumber(self, n:int):
        nums = [1]
        idx_2, idx_3, idx_5 = 0,0,0
        for i in range(n-1):
            next2 = nums[idx_2]*2
            next3 = nums[idx_3]*3
            next5 = nums[idx_5]*5
            next=min(next2,next3,next5)
            nums.append(next)
            if next==next2:
                idx_2+=1
            if next == next3:
                idx_3+=1
            if next == next5:
                idx_5+=1
        return nums[-1]
            
    
    
    
