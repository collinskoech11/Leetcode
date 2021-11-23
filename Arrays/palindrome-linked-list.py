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
        nums= []
        while head:
            nums.append(head.val)
            head = head.next
            
        l,r = 0, len(nums) - 1
        while l<=r:
            if nums[l] != nums[r]:
                return False
            l+=1
            r-=1
        return True
