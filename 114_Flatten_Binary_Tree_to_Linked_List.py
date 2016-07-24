# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.l = []
        if root:
            self.dfs(root)
        for i in xrange(len(self.l) - 1):
            self.l[i].left = None
            self.l[i].right = self.l[i + 1]

    def dfs(self, node):
        self.l.append(node)
        if node.left:
            self.dfs(node.left)
        if node.right:
            self.dfs(node.right)

