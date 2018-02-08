'''
Created on Feb 8, 2018

@author: grekz
'''

class E111_MinimumDepthofBinaryTree:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None) : return 0
        def drill( walk, lvl ):
            if(walk == None) : return 2147483647
            if(walk.left == None and walk.right == None) : return lvl
            return min(drill(walk.left, lvl+1), drill(walk.right, lvl+1))
        return drill(root, 1)
        