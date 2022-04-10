class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curSum):
            if not node:# if root node is empty return False 
                return False
            
            curSum += node.val
            
            if not node.left and not node.right:
                return curSum == targetSum
            
            if dfs(node.left, curSum):
                return True
            
            if dfs(node.right, curSum):
                return True
                    
        return dfs(root, 0)# runs the helper function across the whole tree
