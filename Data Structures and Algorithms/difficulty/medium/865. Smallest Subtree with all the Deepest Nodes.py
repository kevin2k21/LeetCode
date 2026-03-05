from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if root is None:
                return (0,None)
            
            left_depth,left_node = dfs(root.left)
            right_depth,right_node = dfs(root.right)

            if left_depth > right_depth:
                return (left_depth+1,left_node)
            elif right_depth > left_depth:
                return (right_depth+1,right_node)
            else:
                return (left_depth+1,root)
        return dfs(root)[1]

root = TreeNode(5)
root.left = TreeNode(12)
root.right = TreeNode(13)

root.left.left = TreeNode(7)
root.left.right = TreeNode(14)

root.right.right = TreeNode(2)

root.left.left.left = TreeNode(17)
root.left.left.right = TreeNode(23)

root.left.right.left = TreeNode(27)
root.left.right.right = TreeNode(3)

root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(11)


sol = Solution()
print(sol.subtreeWithAllDeepest(root))
