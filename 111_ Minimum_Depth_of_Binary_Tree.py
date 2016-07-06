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
        self.minD = float("inf")
        if not root:
            return 0
        self.minRec(root, 0)
        return self.minD

    def minRec(self, node, num):
        if node.left and node.right:
            self.minRec(node.left, num + 1)
            self.minRec(node.right, num + 1)
        elif node.left == None and node.right != None:
            self.minRec(node.right, num + 1)
        elif node.right == None and node.left != None:
            self.minRec(node.left, num + 1)
        else:
            self.minD = min(self.minD, num + 1)
            