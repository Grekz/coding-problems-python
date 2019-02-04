'''
@author: grekz
'''


class E052_NQueensII:

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        cols = [False] * n
        d1 = [False] * (2*n)
        d2 = [False] * (2*n)
        return self.bt(0, cols, d1, d2, n, 0)

    def bt(self, row, cols, d1, d2, n, count):
        if row == n:
            return count + 1
        for c in range(n):
            id1 = n + c - row
            id2 = c + row
            if not (cols[c] or d1[id1] or d2[id2]):
                cols[c] = True
                d1[id1] = True
                d2[id2] = True
                count = self.bt(row+1, cols, d1, d2, n, count)
                cols[c] = False
                d1[id1] = False
                d2[id2] = False
        return count
