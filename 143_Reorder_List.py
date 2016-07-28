# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        l = []
        node = head
        while node:
            l.append(node)
            node = node.next
        i,j = 0,len(l)-1
        dummy = ListNode(0)
        last = dummy
        while i <= j:
            last.next,l[j].next,l[i].next = l[i],l[i].next,l[j]
            last = l[j]
            i+=1
            j-=1
        last.next = None
        head = dummy.next