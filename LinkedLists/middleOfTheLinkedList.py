"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
class Solution:
 def middleNode(self, head):
  len_list = 0
  start = node = head
  while start:
   len_list += 1
   start = start.next
  middle = len_list // 2
  counter = 0
  while node:
   if counter == middle:
    return node
   else:
    counter += 1
    node = node.next
  return None 
  
  
