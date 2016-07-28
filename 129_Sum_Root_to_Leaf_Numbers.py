# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.cur = []
        self.nums = []
        if not root:
            return 0
        self.dfs(root)
        return sum(self.nums)

    def dfs(self, node):
        self.cur.append(node.val)
        left, right = False, False
        if node.left:
            left = True
            self.dfs(node.left)
        if node.right:
            right = True
            self.dfs(node.right)
        if not left and not right:
            self.nums.append(int(''.join([str(i) for i in self.cur])))
        self.cur.pop()
