'''
@author: grekz
'''


class E526_BeautifulArrangement:

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        return self.permutate(N, 1, 0, [False] * (N + 1))

    def permutate(self, n, pos, count, v):
        if pos > n:
            return count + 1
        for i in range(1, n + 1):
            if not v[i] and (i % pos == 0 or pos % i == 0):
                v[i] = True
                count = self.permutate(n, pos + 1, count, v)
                v[i] = False
        return count
