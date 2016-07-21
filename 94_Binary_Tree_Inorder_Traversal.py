# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        if root:
            self.inord(root)
        return self.res
    def inord(self,node):
        if node.left:
            self.inord(node.left)
        self.res.append(node.val)
        if node.right:
            self.inord(node.right)