"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l3_head = ListNode(0)
        l3_cur = l3_head
        
        while list1 and list2: #assert both exist
            if list2.val < list1.val:
                l3_cur.next = list2 #build l3's node
                list2 = list2.next #this is i++ 
            else:
                l3_cur.next = list1
                list1 = list1.next     
            l3_cur = l3_cur.next #find the next to build
        if list1:
            l3_cur.next = list1 
        if list2:
            l3_cur.next = list2

        return l3_head.next
