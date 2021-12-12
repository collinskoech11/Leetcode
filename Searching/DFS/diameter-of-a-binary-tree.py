class Solution:
    def diameterOfBinaryTree(self, root: Optional[TReeNode]) -> int:
        self.res = 0
        def depth(node):
            if not node:
                return 0
            left_depth=depth(node.left)
            right_depth=depth(node.right)
            self.res = max(self.res, left_depth+right_depth)
            return max(left_depth, right_depth) +1
        depth(root)
        return self.res
            
