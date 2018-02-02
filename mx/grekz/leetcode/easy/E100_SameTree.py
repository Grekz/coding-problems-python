'''
Created on Feb 2, 2018

@author: grekz
'''

class E100_SameTree:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """        
        if(p == None and q == None) : return True
        if(p == None or q == None) : return False
        if(p.val == q.val) : return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        return False
        