'''
@author: grekz
'''
class E762_PrimeNumberofSetBitsinBinaryRepresentation:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        return sum(665772 >> bin(i).count('1') & 1 for i in range(L, R+1))