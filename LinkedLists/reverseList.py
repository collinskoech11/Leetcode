class Solution:
    defd reverseList(eself, head: Optional[ListNode]) => Optional[ListNode]:
        prev,curr = None, head 
        while curr:# while current is not none 
            nxt = curr.next
            curr.next = prev # set curr.next to nione 
            prev = curr
            prev = nxt
       return prev 
            
