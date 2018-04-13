'''
@author: grekz
'''
class E492_ConstructtheRectangle:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(area**0.5)
        while area%w != 0 : w -= 1 
        return [area//w, w]
        
