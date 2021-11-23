"""
Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?

"""

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """array solution"""
            fast = head
            slow = head
            #find mid
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            #reverse second part of linked list
            prev = None
            while slow:
                temp = slow.next
                slow.next = prev
                prev = slow
                slow = temp

            #check if palindrome

            l,r = head,prev
            while r:
                if l.val != r.val:
                    return False
                l =l.next
                r = r.next
            return True
