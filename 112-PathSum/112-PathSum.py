# Last updated: 3/28/2026, 12:55:18 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def hasSum(root,cursum):
            if not root:
                return False

            cursum+=root.val

            if not root.left and not root.right:
                return cursum==targetSum
            
            return hasSum(root.left,cursum) or hasSum(root.right,cursum)
        
        return hasSum(root,0)

        