# Arrays
### 1D array example nums = [1,2,3,4,5] (also nums: list[int])
## indexing 
nums[0] = 1
nums[-1] = 5

### Contains Duplicate
#### given an array nums return True if an element in nums appears atleast twice in the array false if all elements are distinct
[1,2,3,1] returns True [1,2,3,4] returns False 
#### Hash set 
##### 1: convert nums to a hash set then compare the lenghth of the hashset with length of nums if != return True
##### 2: Way create a set .  Run a for loop iterating through elements of nums appending to the set if element does not exist in the set else : return True
#### Time and Space complexity comparison 
##### 1: O(N^3)
##### 2: O(N^2)



