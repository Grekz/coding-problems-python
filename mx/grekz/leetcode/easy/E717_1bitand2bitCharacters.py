'''
@author: grekz
'''
class E717_1bitand2bitCharacters:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n = len(bits) - 1
        if n < 1 : return True
        for i in range(n -1, -1, -1) :
            if bits[i] == 0 :
                return ( n - i ) & 1 == 1
        return ( n - 1 ) & 1 == 1