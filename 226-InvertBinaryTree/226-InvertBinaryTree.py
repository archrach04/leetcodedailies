# Last updated: 3/28/2026, 12:54:55 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        left=self.invertTree(root.left)
        right=self.invertTree(root.right)

        root.right=left
        root.left=right

        return root
        