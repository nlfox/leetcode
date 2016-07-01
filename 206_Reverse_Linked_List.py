# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        l = []
        while p:
            l.append(p)
            p = p.next
        l = l[::-1]
        l.append(None)

        for i in xrange(len(l) - 1):
            l[i].next = l[i + 1]
        return l[0]

