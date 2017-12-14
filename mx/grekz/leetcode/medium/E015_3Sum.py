'''
Created on Dec 14, 2017

@author: grekz
'''
class E015_3Sum:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        le = len(nums)
        res = []
        for i in range( 0, le - 1 ) :
            cur = nums[i]
            if i > 0 and cur == nums[i-1] :
                continue
            l = i + 1
            h = le - 1
            while l < h :
                su = nums[l] + nums[h] + cur
                if  su == 0 :
                    res.append([ cur, nums[l], nums[h] ])
                    while l < h and nums[l] == nums[ l + 1 ] : l += 1;
                    while l < h and nums[h] == nums[ h - 1 ] : h -= 1;
                    h -= 1
                    l += 1
                elif su < 0 :
                    l += 1
                else:
                    h -= 1
        return res