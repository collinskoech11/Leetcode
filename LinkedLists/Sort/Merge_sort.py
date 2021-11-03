
"""
Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
 
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head #if list = null or has one val
        
        p, slow, fast = None, head, head
        while fast and fast.next:
            p = slow
            slow =  slow.next
            fast = fast.next.next
            
        p.next = None 
        
        return self.merge(self.sortList(head), self.sortList(slow))
    
    def merge(self, l1, l2):
        dummy = ListNode(None)
        
        curr = dummy
        
        while l1 and l2:
            if  l1.val > l2.val:
                curr.next, l2 = l2, l2.next
            else:
                curr.next,l1 = l1, l1.next
            curr = curr.next
            
        if l1:
            curr.next =l1
        elif l2:
            curr.next = l2
            
        return dummy.next
        
        
        
