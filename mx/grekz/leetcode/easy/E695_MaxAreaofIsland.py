'''
@author: grekz
'''
class E695_MaxAreaofIsland:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.n = len(grid)
        self.m = len(grid[0])
        def doit(row, col) :
            if row < 0 or col < 0 or row >= self.n or col >= self.m or grid[row][col] == 0 :
                return 0
            grid[row][col] = 0
            return 1 + doit(row-1,col) + doit(row+1,col) + doit(row ,col - 1) + doit(row,col + 1)
        return max([0] + [doit(i,j) for i in range(self.n) for j in range(self.m) if grid[i][j] ])
        