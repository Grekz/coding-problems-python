'''
@author: grekz
'''
class E0892_SurfaceAreaof3DShapes:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n, ans = len(grid), 0
        for i in range(n) :
            for j in range(n) :
                v = grid[i][j]
                if ( v > 0 ) :
                    ans += 4 * v + 2
                if ( i > 0 ) :
                    ans -= min(v, grid[i-1][j]) * 2
                if ( j > 0 ) :
                    ans -= min(v, grid[i][j-1]) * 2
        return ans