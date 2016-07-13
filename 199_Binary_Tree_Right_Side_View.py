# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = {}
        if not root:
            return []
        self.dfs(root, 0)
        return [self.res[i] for i in xrange(len(self.res))]

    def dfs(self, node, level):
        self.res[level] = node.val
        if node.left:
            self.dfs(node.left, level + 1)
        if node.right:
            self.dfs(node.right, level + 1)

