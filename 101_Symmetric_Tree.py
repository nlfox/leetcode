# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q = [(root, 0)]
        res = {}
        while q:
            node, level = q.pop(0)
            if not node:
                v = None
            else:
                v = node.val
            if level in res:
                res[level] += [v]
            else:
                res[level] = [v]
            if not node:
                continue
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))
        t = [res[i] for i in xrange(len(res))]
        for i in t:
            if i[::-1] != i:
                return False
        return True
