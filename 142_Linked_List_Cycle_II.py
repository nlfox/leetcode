# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            l = {}
            while head:
                if l.has_key(head):
                    return head
                l[head] = True
                head = head.next

        except:
            return None
