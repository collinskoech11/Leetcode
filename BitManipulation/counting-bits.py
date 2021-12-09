class Solution:
    def countingBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        
        offset = 1
        
        for i in range(1, n+ 1):
            if offset * 2 == i:
                offset = 1
            output[i] = 1 + output[i - offset]
                
        return output
