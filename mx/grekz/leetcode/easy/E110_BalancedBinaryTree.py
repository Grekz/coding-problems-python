'''
Created on Feb 12, 2018

@author: grekz
'''

class E110_BalancedBinaryTree:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if ( root == None ) : return 0 
            lh = dfs(root.left)
            if ( lh == -1 ) : return -1
            rh = dfs(root.right)
            if ( rh == -1 ) : return -1
            dif = lh - rh
            if ( dif > 1 or dif < -1 ) : return -1 
            return max(lh, rh) + 1
        return dfs(root) != -1
        
        