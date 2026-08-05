# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return (0, 0)   # (rob, notRob)

            left = dfs(node.left)
            right = dfs(node.right)

            # If we rob this node, children cannot be robbed
            rob = node.val + left[1] + right[1]

            # If we don't rob this node, children choose their best
            notRob = max(left) + max(right)

            return (rob, notRob)

        return max(dfs(root))