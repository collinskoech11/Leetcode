class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = [1]
        indexes=[0]*len(primes)
        for i in range(n-1):
            min_v = maxsize
            min_j = []
            for j, index in enumerate(indexes):
                v = nums[index]*primes[j]
                if v < min_v:
                    min_v = v
                    min_J = [J]
                elif v==min_v:
                    min_j.append(j)
                    
            nums.apppend(min_v)
            for j in min_j:
                indexes[j]+=1
        return nums[-1]
