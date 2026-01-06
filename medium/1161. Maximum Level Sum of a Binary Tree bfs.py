from typing import Optional

# Definition for a binary tree TreeNode.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        max_val = float('-inf')
        res = 0
        lvl = 1
        while queue:
            next_level = []
            cur_val  = 0
            for node in queue:
                cur_val += node.val

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            if max_val < cur_val:
                max_val = cur_val
                res = lvl

            lvl += 1
            queue = next_level
        return res
        


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
