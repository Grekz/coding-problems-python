'''
@author: grekz
'''
class E783_MinimumDistanceBetweenBSTNodes:

    res, pre = 2147483647, -1
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root :
            return self.res
        self.minDiffInBST(root.left)
        if self.pre > -1 :
            self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        print(str(self.res) + '---' + str(root.val))
        self.minDiffInBST(root.right)
        return self.res