# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        last = head.val
        p = head.next
        pr = head
        while p:
            if p.val != last:
                pr.next = p
                pr = p
                last = p.val
            else:
                pr.val = "d"
            p = p.next
        pr.next = None
        p = head.next
        preP = head
        while p:
            if p.val == "d":
                preP.next = p.next
            else:
                preP = preP.next
            p = p.next
        preP.next = None
        if head.val == "d":
            head = head.next
        return head
