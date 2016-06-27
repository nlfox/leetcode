class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            l = {}
            while head:
                if l.has_key(str(head)):
                    return head
                l[str(head)] = True
                head = head.next

        except:
            return None