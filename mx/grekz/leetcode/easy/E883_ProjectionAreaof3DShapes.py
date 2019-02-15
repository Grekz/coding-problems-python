'''
@author: grekz
'''


class E883_ProjectionAreaof3DShapes:

    def projectionArea(self, grid: 'List[List[int]]') -> 'int':
        res, n = 0, len(grid)
        for i in range(n):
            col, row = 0, 0
            for j in range(n):
                if grid[i][j] > 0:
                    res += 1
                row = max(row, grid[i][j])
                col = max(col, grid[j][i])
            res += row + col
        return res
