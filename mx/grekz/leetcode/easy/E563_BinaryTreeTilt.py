'''
@author: grekz
'''
class E563_BinaryTreeTilt:

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.su = 0
        def doit(n) :
            if not n : return 0
            left, right = doit(n.left), doit(n.right)
            self.su += abs(left-right)
            return n.val + left + right
        doit(root)
        return self.su