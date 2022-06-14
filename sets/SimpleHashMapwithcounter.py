class Solution:
  def SimpleHash(self, my_list:List[int]) -> int:
    freq = {}# initialize a dictionary
    for item in my_list# iterate through items in the list
      if item in freq:# check if item already exists in the dict
        freq[item] += 1#increment
      else:
        freq[item] = 1# initialize it in the dict
    for key, value in freq.items():# separate key from values in the dict
      print(key, value)
