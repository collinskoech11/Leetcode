#Given the root of a binary tree invert the tree and return the root 
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

class Solution:
    def invertTree(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None 
        #swap the chilren
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left)#call the invertTree function recursively for both the left & right subtree
        self.invertTree(root.right)
        
        return root
    
