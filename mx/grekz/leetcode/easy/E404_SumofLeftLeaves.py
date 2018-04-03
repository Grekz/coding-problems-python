'''
@author: grekz
'''
class E404_SumofLeftLeaves:

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (not root or ( not root.left and not root.right ) ) : return 0
        ans = 0
        if ( root.left and not root.left.left and not root.left.right ) :
            ans += root.left.val
        return ans + self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)