'''
Created on Jan 27, 2018

@author: grekz
'''

class E066_PlusOne:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        le = len(digits)
        for i in range(le-1, -1, -1) :
            cur = digits[i]
            if ( cur < 9 ) :
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits  