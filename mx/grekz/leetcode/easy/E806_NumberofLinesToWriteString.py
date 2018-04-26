'''
@author: grekz
'''
class E806_NumberofLinesToWriteString:

    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        
        lastLength = 0
        lines = 0
        for c in S :
            curWidth = widths[ord(c) - 97]
            if (lastLength + curWidth > 100):
                lines += 1
                lastLength = curWidth
            else :
                lastLength += curWidth
            
        if ( lastLength < 100 ) :
            lines += 1 
        return [lines, lastLength]