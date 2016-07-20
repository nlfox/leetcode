class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        pass
        self.cur = []
        self.res = []
        if root:
            self.dfs(root)
        return self.res

    def dfs(self,node):
        if not node.left and not node.right:
            self.cur.append(node.val)
            self.res.append("->".join([str(i) for i in self.cur]))
            self.cur.pop()
        if node.left:
            self.cur.append(node.val)
            self.dfs(node.left)
            self.cur.pop()
        if node.right:
            self.cur.append(node.val)
            self.dfs(node.right)
            self.cur.pop()