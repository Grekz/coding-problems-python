'''
@author: grekz
'''
class E414_ThirdMaximumNumber:

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = m2 = m3 = None
        for x in nums:
            if x == m1 or x == m2 or x == m3:
                continue
            if ( m1 == None or x > m1 ) :
                m3 = m2
                m2 = m1
                m1 = x
            elif ( m2 == None or x > m2 ) :
                m3 = m2
                m2 = x
            elif ( m3 == None or x > m3 ) :
                m3 = x
        if m3 is None:
            return m1
        return m3