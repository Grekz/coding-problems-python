'''
@author: grekz
'''

class E219_ContainsDuplicateII:

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if(k == 0 or nums == None or len(nums) < 2 ) : return False
        values = {}
        for i, x in enumerate(nums):
            if(x in values and i - values[x] <= k  ) :
                return True
            values[x] = i
        return False