'''
@author: grekz
'''
class E075_SortColors:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def swap(a,b,n) :
            t = n[a]
            n[a] = n[b]
            n[b] = t
        i, j, k = 0, 0, len(nums) - 1
        while i <= k :
            if nums[i] == 0 :
                swap(i, j, nums)
                j += 1
            elif nums[i] == 2 : 
                swap(i, k, nums)
                i -= 1
                k -= 1
            i += 1