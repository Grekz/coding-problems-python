'''
@author: grekz
'''
class E538_ConvertBSTtoGreaterTree:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.cur = 0
        def go(x):
            if not x : return
            go(x.right)
            x.val += self.cur
            self.cur = x.val
            go(x.left)
        go(root)
        return root