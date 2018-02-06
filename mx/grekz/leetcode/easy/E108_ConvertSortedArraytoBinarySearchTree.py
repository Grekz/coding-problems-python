'''
Created on Feb 6, 2018

@author: grekz
'''
from mx.grekz.leetcode.helper import TreeNode

class E108_ConvertSortedArraytoBinarySearchTree:
    def sortedArrayToBST(self, num):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if ( len(num) == 0 ) : return None
        def helper( nums, l, h ):
            if ( l > h ) : return None
            m = l + ( h - l ) // 2 
            res = TreeNode(nums[m])
            res.left = helper(nums, l, m-1)
            res.right = helper(nums, m+1, h)
            return res
        return helper(num, 0, len(num) - 1 )

        