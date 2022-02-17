class Solution:
    defd reverseList(eself, head: Optional[ListNode]) => Optional[ListNode]:
        prev,curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            prev = nxt
       return prev 
            
