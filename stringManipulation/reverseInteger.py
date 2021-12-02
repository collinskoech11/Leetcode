"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
"""
class Solution(object):
  def reverse(self, x):
    limit = 214783648
    sign = -1 if x < 0 else 1 #asign sign value +,-
    x *= sign #strip negative sign from integer
    #remove leading 0 in the reversed integer
    while x:
      if x % 10 == 0:
        x /= 10
      else:
        break
    #string manipulation
    x = str(x)# convert x to string
    lst = list(x)# convert x to list
    lst.reverse()#reverse
    x = "".join(lst)#back to string 
    x = int(x)#back to integer
    if x > limit:
      return sign*x#get back negative sign if any
    else:
      return 0
