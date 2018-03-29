'''
@author: grekz
'''
class E485_MaxConsecutiveOnes:

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        cur = ma = 0
        for x in nums:
            if ( x == 1 ) :
                cur+=1
            else :
                cur = 0
            if ( ma < cur ) :
                ma = cur
        return ma