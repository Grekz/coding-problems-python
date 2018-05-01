'''
@author: grekz
'''
class E693_BinaryNumberwithAlternatingBits:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        b = bin(n)
        return '11' not in b and '00' not in b 