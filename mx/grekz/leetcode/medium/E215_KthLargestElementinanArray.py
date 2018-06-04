'''
@author: grekz
'''
class E215_KthLargestElementinanArray:

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[-k]