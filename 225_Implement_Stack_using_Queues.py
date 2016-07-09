class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        while self.s1:
            self.s2.append(self.s1.pop(0))
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop(0))


    def pop(self):
        """
        :rtype: nothing
        """
        return self.s1.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.s1[0]


    def empty(self):
        """
        :rtype: bool
        """
        return True if self.s1 == [] else Fal