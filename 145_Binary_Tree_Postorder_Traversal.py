# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        if root:
            self.post(root)
        return self.res

    def post(self, node):
        if node.left:
            self.post(node.left)
        if node.right:
            self.post(node.right)
        self.res.append(node.val)


