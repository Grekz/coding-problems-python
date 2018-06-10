'''
@author: grekz
'''
class E807_MaxIncreasetoKeepCitySkyline:

    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m, res = len(grid), len(grid[0]), 0
        r, c = [0] * n, [0] * m
        for i in range(n) :
            for j in range(m) :
                if r[i] < grid[i][j] :
                    r[i] = grid[i][j]
                if c[j] < grid[i][j] :
                    c[j] = grid[i][j]
        for i in range(n) :
            for j in range(m) :
                res += min(r[i], c[j]) - grid[i][j]
        return res