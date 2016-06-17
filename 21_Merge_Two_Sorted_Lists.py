# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def construct(l):
    res = ListNode(l[0])
    head = res
    for i in l[1:]:
        res.next = ListNode(i)
        res = res.next
    return head


def pri(node):
    p = node
    while p:
        print p.val,
        p = p.next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        new = None
        head = None
        if p1 and p2:
            new = ListNode(p2.val) if p1.val > p2.val else ListNode(p1.val)
            head = new
            if p1.val > p2.val:
                p2 = p2.next
            else:
                p1 = p1.next
            while p1 and p2:
                if p1.val > p2.val:
                    new.next = ListNode(p2.val)
                    new = new.next
                    p2 = p2.next
                else:
                    new.next = ListNode(p1.val)
                    new = new.next
                    p1 = p1.next
            if p1:
                new.next = p1
            if p2:
                new.next = p2
        else:
            head = p1 if p1 else p2
        return head

pri(Solution().mergeTwoLists(construct([1, 2, 3]),construct([2, 3, 4])))
