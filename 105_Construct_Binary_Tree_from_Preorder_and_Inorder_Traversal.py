# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        return self.build(0,len(preorder),0,len(inorder))
    def build(self, pres,pree,ins,ine):
        if pres>=pree and ins>=ine:
            return None
        mid = self.preorder[pres]
        pos = self.inorder.index(mid)-ins
        node = TreeNode(mid)
        node.left = self.build(pres+1,pres+1+pos,ins,ins+pos)
        node.right = self.build(pres+pos+1,pree,ins+pos+1,ine)
        return node