class ListNode(object):
    def __init__(self, key,val):
        self.val, self.key = val,key
        self.prev, self.next = None, None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = ListNode(-1,-1)
        self.head.next, self.head.prev = self.head, self.head
        self.capacity = capacity
        self.keymap = {}
        self.size = 0

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.keymap:
            return -1
        cur = self.keymap[key]
        prev, next = cur.prev, cur.next
        if prev == self.head: # first node here, just return val
            return cur.val
        prev.next = next
        next.prev = prev
        cur.next = self.head.next
        self.head.next.prev = cur
        cur.prev = self.head
        self.head.next = cur
        return cur.val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.keymap:
            if self.size == self.capacity:
                del self.keymap[self.head.prev.key]
                self.head.prev.prev.next = self.head
                self.head.prev = self.head.prev.prev
                self.size -= 1
            self.keymap[key] = ListNode(key, value)
            cur = self.keymap[key]
            self.size += 1
        else:
            cur = self.keymap[key]
            cur.val = value
            prev, next = cur.prev, cur.next # mark the previous and next node of cur node
            prev.next, next.prev = next, prev
        cur.next = self.head.next
        self.head.next.prev = cur
        cur.prev = self.head
        self.head.next = cur