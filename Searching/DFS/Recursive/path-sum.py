"""Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curSum):
            if not root:
                return False
            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum

            return (dfs(node.left, curSum) or dfs(node.right, curSum))

        return dfs(root, 0)
#start with targetSum then subtract the value of the node from the targetSum return True if the difference is 0
class SolutionTwo:
    def hasPathSum(self, root:OPtional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= node.val
        if not root.left and not root.right:
            return targetSum==0
        else:
            return self.hasPathSum(root,left,targetSum) or self.hasPathSum(root.right,targetSum)
        
