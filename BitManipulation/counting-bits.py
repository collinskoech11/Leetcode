class Solution:
    def countingBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        
        offset = 1
        
        for i in range(1, n+ 1):
            of offset * 2 == i:
                offset = 1
                
        return output
