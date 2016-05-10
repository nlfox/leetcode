class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root:
            self.res = [[]]
        else:
            return []
        self.maxLevel = 0
        self.bfs(root, 0)
        for i in range(self.maxLevel+1):
            if i%2:
                self.res[i]=self.res[i][::-1]
        return self.res

    def bfs(self, node, level):
        if level > self.maxLevel:
            self.res.append([node.val])
            self.maxLevel += 1
        else:
            self.res[level] += [node.val]
        if node.left:
            self.bfs(node.left, level + 1)
        if node.right:
            self.bfs(node.right, level + 1)
        return