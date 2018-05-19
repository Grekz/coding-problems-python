'''
@author: grekz
'''
class E572_SubtreeofAnotherTree:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s: return False
        def isSame(a,b):
            if not a and not b : return True
            if a == None or b == None : return False
            return a.val == b.val and isSame(a.left,b.left) and isSame(a.right,b.right)
        return isSame(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right,t)
        