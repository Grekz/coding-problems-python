'''
Created on Feb 9, 2018

@author: grekz
'''

class E112_PathSum:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if ( root == None ) : return False
        sumOk = sum - root.val == 0 and root.left == None and root.right == None
        remain = sum - root.val
        return sumOk or self.hasPathSum(root.left, remain) or self.hasPathSum(root.right, remain)