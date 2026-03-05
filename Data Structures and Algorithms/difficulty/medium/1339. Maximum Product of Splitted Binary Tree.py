from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sum = []
        dfs(root,subtree_sum)
        m = subtree_sum.pop(-1)
        res = float('-inf')
        for i in subtree_sum:
            res = max(res,i*(m-i))
        return res%(10**9+7)


        
def dfs(root,subtree_sum):
    if root is None:
        return 0

    left_sum = dfs(root.left,subtree_sum)
    right_sum = dfs(root.right,subtree_sum)

    total = left_sum+right_sum+root.val
    subtree_sum.append(total)

    return total
