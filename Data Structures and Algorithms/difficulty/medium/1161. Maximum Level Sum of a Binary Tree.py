from typing import Optional

# Definition for a binary tree TreeNode.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = []
        level = 0
        dfs(root,res,level)
        m = max(res)
        return res.index(m)+1

        
def dfs(root,res,level):
    if root is None:
        return
    
    if len(res) == level:
        #res.append([])
        res.append(0)

    #res[level].append(root.val)
    res[level] += root.val
    
    dfs(root.left,res,level+1)
    dfs(root.right,res,level+1)


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
print(sol.maxLevelSum(root))
