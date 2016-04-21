# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = 0
        if root:
            self.dfs(root, 0)
        return self.depth

    def dfs(self, node, count):
        if count > self.depth:
            self.depth = count
        if node.left:
            self.dfs(node.left, count + 1)
        if node.right:
            self.dfs(node.right, count + 1)
        return
