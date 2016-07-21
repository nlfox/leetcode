# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        if root:
            self.pre(root)
        return self.res

    def pre(self, node):
        self.res.append(node.val)
        if node.left:
            self.pre(node.left)
        if node.right:
            self.pre(node.right)
