'''
@author: grekz
'''
class E334_IncreasingTripletSubsequence:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a, b = 2147483647, 2147483647
        for x in nums :
            if x <= a :
                a = x
            elif x <= b :
                b = x
            else :
                return True
        return False