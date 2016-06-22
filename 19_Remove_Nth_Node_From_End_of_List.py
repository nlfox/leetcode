# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        h = head
        l = []
        while h:
            l.append(h)
            h = h.next
        if len(l) == 1:
            return None
        if n == len(l):
            return l[1]
        l[-n - 1].next = l[-n].next
        return head
