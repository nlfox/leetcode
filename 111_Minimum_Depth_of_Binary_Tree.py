# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = float("inf")
        if not root:
            return 0
        self.dfs(root, 1)
        return self.depth

    def dfs(self, node, count):
        if not node.left and not node.right:
            if count <= self.depth:
                self.depth = count
        else:
            if node.left:
                self.dfs(node.left, count + 1)
            if node.right:
                self.dfs(node.right, count + 1)