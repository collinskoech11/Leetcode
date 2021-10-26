"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1
"""

#isBadVersion has already been decared
# @param version, an integer 
# @return bool
# def isBadVersion(version):


class Solution(object):
  def firstBadVersion(self, n):
    """
    :type n:int
    :rtype: int
    """
    
    start = 1
    end = n # pointers
    while start < end :
      mid = (start + end)//2
      if isBadVersion(mid):
        end = mid # if true search in first part 
      else:
        start = mid + 1 # if false search in second part
    return start
