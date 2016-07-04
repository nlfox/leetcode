class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        s = ((abs(C - A) * abs(D - B)) + (abs(G - E) * abs(H - F)))
        if E > C or F > D or G < A or H < B:
            return s
        I, J = max(A, E), max(B, F)
        K, L = min(C, G), min(D, H)
        return s - (K - I) * (L - J)
