# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        node  = head
        l = []
        while node:
            l.append(node)
            node = node.next
        lt = []
        ge = []
        for i in l:
            if i.val < x:
                lt.append(i)
            else:
                ge.append(i)
        dummy = ListNode(0)
        r = [dummy] + lt + ge
        for i,v in enumerate(r):
            if i == 0:
                continue
            r[i-1].next = v
        r[-1].next = None
        return dummy.next