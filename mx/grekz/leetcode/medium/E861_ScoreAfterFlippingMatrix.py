'''
@author: grekz
'''


class E861_ScoreAfterFlippingMatrix:

    def matrixScore(self, a: 'List[List[int]]') -> 'int':
        rows, cols = len(a), len(a[0])
        ans = 0
        for c in range(cols):
            col = 0
            for r in range(rows):
                col += a[r][c] ^ a[r][0]
            ans += max(col, rows - col) * (1 << (cols - c - 1))
        return ans
