'''
Created on Dec 3, 2017
https://leetcode.com/problems/two-sum/description/

@author: grekz
'''
class E001_TwoSum:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        i = 0
        for x in nums:
            if target - x in dic:
                return [dic[target - x], i]
            else:
                dic[x] = i
            i+=1
        return [0,0]