# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        self.nums = nums
        return self.rec(0, len(nums) - 1)

    def rec(self, left, right):
        if left > right:
            return None
        mid = (left + right) / 2
        node = TreeNode(self.nums[mid])
        node.left = self.rec(left, mid - 1)
        node.right = self.rec(mid + 1, right)
        return node