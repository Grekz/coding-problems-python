'''
@author: grekz
'''
class E733_FloodFill:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == newColor :
            return image
        self.dfs(image, sr, sc, image[sr][sc], newColor)
        return image
        
    def dfs(self, tmp, a, b, c, d) :
        if a < 0 or b < 0 or a >= len(tmp) or b >= len(tmp[0]) or tmp[a][b] != c :
            return 
        tmp[a][b] = d
        self.dfs(tmp, a, b-1, c, d)
        self.dfs(tmp, a, b+1, c, d)        
        self.dfs(tmp, a-1, b, c, d)        
        self.dfs(tmp, a+1, b, c, d)