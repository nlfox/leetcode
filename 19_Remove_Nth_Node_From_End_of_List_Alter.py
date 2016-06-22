# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start = ListNode(0)
        f, s = start, start
        start.next = head
        for i in xrange(n + 1):
            f = f.next
        while f:
            f = f.next
            s = s.next
        s.next = s.next.next

        return start.next