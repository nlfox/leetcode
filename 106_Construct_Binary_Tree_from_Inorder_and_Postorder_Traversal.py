# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.inorder = inorder
        self.postorder = postorder
        return self.build(0,len(inorder),0,len(postorder))
    def build(self, ins,ine,posts,poste):
        if ins>=ine and posts>=poste:
            return None
        mid = self.postorder[poste-1]
        pos = self.inorder.index(mid)-ins
        node = TreeNode(mid)
        node.left = self.build(ins,ins+pos,posts,posts+pos)
        node.right = self.build(ins+pos+1,ine,posts+pos,poste-1)
        return node