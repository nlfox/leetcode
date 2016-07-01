# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        p = head
        l = []
        while p:
            l.append(p)
            p = p.next
        l = [None] + l + [None]
        lr = l[m:n + 1][::-1]
        if l[m - 1]:
            l[m - 1].next = lr[0]
        else:
            head = lr[0]
        for i in xrange(len(lr) - 1):
            lr[i].next = lr[i + 1]
        lr[-1].next = l[n + 1]

        return head
