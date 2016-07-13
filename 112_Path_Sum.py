# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        val = sum - root.val
        if val == 0 and root.left == None and root.right == None:
            return True
        return self.hasPathSum(root.left, val) or self.hasPathSum(root.right, val)
