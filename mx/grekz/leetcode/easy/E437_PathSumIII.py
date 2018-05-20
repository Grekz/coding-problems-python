'''
@author: grekz
'''
class E437_PathSumIII:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root : return 0
        def doit(n, s):
            if not n : return 0
            return (1 if s == n.val else 0 ) + doit(n.left, s - n.val ) + doit(n.right, s - n.val )
        return doit(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)