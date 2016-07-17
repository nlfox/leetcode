# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        node = head
        n = 0
        while node:
            last = node
            node = node.next
            n += 1
        if k >= n:
            k = k % n
        node = head
        for i in xrange(n - k - 1):
            node = node.next
        last.next = head
        head = node.next
        node.next = None
        return head

