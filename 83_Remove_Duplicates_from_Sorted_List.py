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
            p = p.next
        pr.next = None
        return head