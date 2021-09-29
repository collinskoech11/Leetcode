class Solution(object):
  def romanToInt(self, s):
    value = {
      'M':1000,
      'D':500,
      'C':100,
      'L':50,
      'X':10,
      'V':5,
      'I':1
    }
    P=0
    ans = 0
    # traverse through all the characters 
    n = len(s)
    for i in range(n-1, -1, -1):
      if value[s[i]] >= p:
        ans += value[s[i]]
      else:
        ans -= value[s[i]]
      p = value[s[i]]
    return ans 
    
