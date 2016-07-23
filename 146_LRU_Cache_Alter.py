class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = {}
        self.cap = capacity
        self.l = []

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.d:
            self.l[self.d[key]][1] += 1
            p = self.d[key]
            while p > 0:
                if self.l[p][1] >= self.l[p - 1][1]:
                    self.l[p], self.l[p - 1] = self.l[p - 1], self.l[p]
                    p -= 1
                else:
                    self.d[key] = p
                    break
            if p == 0:
                self.d[key] = 0
            return self.l[self.d[key]][0]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.d:
            self.l[self.d[key]][0] = value
        else:
            if len(self.l) == self.cap:
                self.d.pop(self.l[-1][2])
                self.l.pop()
            self.l.append([value, 0, key])
            self.d[key] = len(self.l) - 1