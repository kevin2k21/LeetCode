from optparse import Values
from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = []
        level = 0
        dfs(root,res,level)

        
def dfs(root,res,level):
    if root is None:
        return
    
    if len(res) == level:
        res.append([])

    res[level].append(root.val)
    
    dfs(root.left,res,level+1)
    
    dfs(root.right,res,level+1)

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)

root.left.left = TreeNode(0)
root.left.right = TreeNode(1)

root.right.left = TreeNode(0)
root.right.right = TreeNode(1)


sol = Solution()
print(sol.sumRootToLeaf(root))
