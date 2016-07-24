# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node = head
        l = []
        while node:
            if node.val != val:
                l.append(node)
            node = node.next
        if len(l) == 0:
            return None
        for i in xrange(len(l)-1):
            l[i].next = l[i+1]
        l[-1].next = None
        return l[0]