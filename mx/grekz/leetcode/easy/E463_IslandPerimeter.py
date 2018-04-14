'''
@author: grekz
'''
class E463_IslandPerimeter:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lenA = len(grid)
        lenB = len(grid[0])
        neig = 0
        islands = 0
        for i in range(lenA):
            for j in range(lenB):
                if (grid[i][j] == 1):
                    islands+=1
                    if ( i < lenA - 1 and grid[i + 1][j] == 1):
                        neig+=1
                    if ( j < lenB - 1 and grid[i][j + 1] == 1): 
                        neig+=1
        return islands * 4 - neig * 2
