#LeetCode Problem 103
#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#Asked during Microsoft Phone Interview

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        