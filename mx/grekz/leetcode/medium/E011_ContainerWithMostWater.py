'''
Created on Dec 10, 2017

@author: grekz
'''
class E011_ContainerWithMostWater:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        hl = len(height)
        if hl < 2: 
            return 0
        l = res = 0
        h = hl - 1
        while l < h :
            res = max( min( height[l], height[h] ) * ( h - l ), res )
            if height[l] < height[h] : 
                l += 1
            else:
                h -= 1
        return res
        