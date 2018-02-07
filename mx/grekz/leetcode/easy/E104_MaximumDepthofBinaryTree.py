'''
Created on Feb 7, 2018

@author: grekz
'''

class E104_MaximumDepthofBinaryTree:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None): return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return ( left if left > right else right ) +1;