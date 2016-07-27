# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.preorderTraversal(root)
        self.inorderTraversal(root)
        return str({"pre": self.preOrderList, "in": self.inOrderList})

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.preOrderList = []
        if root:
            self.pre(root)

    def pre(self, node):
        self.preOrderList.append(node.val)
        if node.left:
            self.pre(node.left)
        if node.right:
            self.pre(node.right)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inOrderList = []
        if root:
            self.inord(root)

    def inord(self, node):
        if node.left:
            self.inord(node.left)
        self.inOrderList.append(node.val)
        if node.right:
            self.inord(node.right)

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        return self.build(0, len(preorder), 0, len(inorder))

    def build(self, pres, pree, ins, ine):
        if pres >= pree and ins >= ine:
            return None
        mid = self.preorder[pres]
        pos = self.inorder.index(mid) - ins
        node = TreeNode(mid)
        node.left = self.build(pres + 1, pres + 1 + pos, ins, ins + pos)
        node.right = self.build(pres + pos + 1, pree, ins + pos + 1, ine)
        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        d = eval(data)
        return self.buildTree(d["pre"], d["in"])


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))