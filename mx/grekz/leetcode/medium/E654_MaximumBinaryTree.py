'''
@author: grekz
'''
from mx.grekz.leetcode.helper import TreeNode
class E654_MaximumBinaryTree:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """   
        if not nums:
            return None
        i = nums.index(max(nums))
        root = TreeNode(nums[i])
        root.left = self.constructMaximumBinaryTree(nums[:i])
        root.right = self.constructMaximumBinaryTree(nums[i+1:])
        return root