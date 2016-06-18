# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1, n2 = [], []
        while l1:
            n1.append(l1.val)
            l1 = l1.next
        while l2:
            n2.append(l2.val)
            l2 = l2.next

        flow = 0
        if len(n1) > len(n2):
            nl, ns = n1, n2
        else:
            nl, ns = n2, n1
        res = []
        for i, v in enumerate(ns):
            s = v + nl[i] + flow
            if s >= 10:
                flow = 1
                s = s - 10
            else:
                flow = 0
            res.append(s)

        for i in xrange(len(ns), len(nl)):
            s = nl[i] + flow
            if s >= 10:
                flow = 1
                s -= 10
            else:
                flow = 0
            i += 1
            res.append(s)
        if flow > 0:
            res.append(flow)
        new = ListNode(res[0])
        head = new
        for i in res[1:]:
            new.next = ListNode(i)
            new = new.next
        return head
