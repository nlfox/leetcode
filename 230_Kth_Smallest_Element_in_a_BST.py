# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = k
        self.l = []
        node = root
        self.dfs(node)
        return self.l[k - 1]

    def dfs(self, node):
        if node.left:
            self.dfs(node.left)
        if self.count > 0:
            self.l.append(node.val)
            self.count -= 1
        else:
            return
        if node.right:
            self.dfs(node.right)

import re
re.m