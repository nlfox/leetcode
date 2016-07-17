# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [(root, 0)]
        res = {}
        while q:
            node, level = q.pop(0)
            if level in res:
                res[level] += [node.val]
            else:
                res[level] = [node.val]
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return [res[i] for i in xrange(len(res))]
