# Last updated: 3/30/2026, 11:28:49 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        maxDiameter=0
10        def height(node):
11            nonlocal maxDiameter
12            if node is None:
13                return 0
14            else:
15                leftHeight=height(node.left)
16                rightHeight=height(node.right)
17                maxDiameter=max(leftHeight+rightHeight,maxDiameter)
18
19                return 1+max(leftHeight,rightHeight)
20        height(root)
21        return maxDiameter
22        