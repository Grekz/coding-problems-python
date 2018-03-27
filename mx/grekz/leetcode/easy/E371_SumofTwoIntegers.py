'''
@author: grekz
'''
class E371_SumofTwoIntegers:

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= MAX else ~(a ^ mask)