'''
Created on Feb 3, 2018

@author: grekz
'''

class E101_SymmetricTree:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(l, r):
            if ( l == None and r == None ) : return True
            if ( l == None or r == None ) : return False
            return l.val == r.val and isMirror(l.left, r.right) and isMirror(l.right, r.left)
        if (root == None) : return True
        return isMirror(root.left, root.right)

        