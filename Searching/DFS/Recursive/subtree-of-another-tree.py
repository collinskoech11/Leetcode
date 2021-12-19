# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def areIdentical(self, T, S):
        # Base Case
        if T is None and S is None:
            return True
        if T is None or S is None:
            return False

        # Check if the val of both roots is same and val of
        # left and right subtrees are also same
        return (T.val == S.val and
                self.areIdentical(T.left , S.left)and
                self.areIdentical(T.right, S.right)
                )
    def isSubtree(self, T: Optional[TreeNode], S: Optional[TreeNode]) -> bool:
        if S is None:
            return True
        if T is None:
            return False

        # Check the tree with root as current node
        if (self.areIdentical(T, S)):
            return True

        # IF the tree with root as current node doesn't match
        # then try left and right subtreee one by one
        return self.isSubtree(T.left, S) or self.isSubtree(T.right, S)
    
    
        """if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False
        if root.val == subRoot.val and self.rootSubtree(root.right, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def rootSubtree(self, root, subRoot):
        if root == None and subroot == None:
            return False
        if root == None or subRoot == None or root.val != subRoot.val:
            return True
        return self.rootSubTree(root.left, subRoot.left) and self.rootSubTree(root.right, subRoot.right)"""
        """if s == None:
            return False
        if self.isSame(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    
    def isSame(self, s, t):
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False
        if s.val != t.val:
            return False
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)"""
        
        
