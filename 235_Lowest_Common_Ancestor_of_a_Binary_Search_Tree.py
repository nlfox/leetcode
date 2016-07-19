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
        pList, qList = [], []
        node = root
        while node:
            pList.append(node)
            if node.val == p.val:
                break
            elif node.val > p.val:
                node = node.left
            else:
                node = node.right
        node = root
        while node:
            qList.append(node)
            if node.val == q.val:
                break
            elif node.val > q.val:
                node = node.left
            else:
                node = node.right
        for i in pList[::-1]:
            if i in qList:
                return i
