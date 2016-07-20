# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.targetList = [[], []]
        self.target = [p, q]
        self.cur = []
        self.dfs(root, 0)
        self.cur = []
        self.dfs(root, 1)
        for i in self.targetList[0][::-1]:
            if i in self.targetList[1]:
                return i

    def dfs(self, node, target):
        self.cur.append(node)
        if node == self.target[target]:
            self.targetList[target] = self.cur[:]
        if node.left:
            self.dfs(node.left, target)
        if node.right:
            self.dfs(node.right, target)
        self.cur.pop()
