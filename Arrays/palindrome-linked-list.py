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
        nums= []#create an empty array nums 
        while head:
            nums.append(head.val)#apend the current head
            head = head.next #go to the next element in the linked list
            
        l,r = 0, len(nums) - 1 #ceate left and right pointers
        while l<=r:
            if nums[l] != nums[r]:
                return False#return false if the element at the right and left pointers are not the same (the linked list is not a palid=ndrome 
            l+=1#move left pointer one step to the right
            r-=1#move the right pointer one step towards the left
        return True# if l > or = to r the linked list is a palindrome after traversing through all the elements  
