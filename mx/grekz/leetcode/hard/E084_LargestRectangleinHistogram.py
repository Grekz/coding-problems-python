'''
@author: grekz
'''
class E084_LargestRectangleinHistogram:

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        heights += [0]
        n = len(heights)
        res = 0
        stack = [-1]
        for i,x in enumerate(heights):
            while x < heights[stack[-1]] :
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack += [i]
        return res