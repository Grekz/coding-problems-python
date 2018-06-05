'''
@author: grekz
'''
class E102_BinaryTreeLevelOrderTraversal:

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root:
            self.doit(res, root, 0)
        return res        
        
    def doit(self, res, walk, lvl):
        if len(res) <= lvl :
            res.append([])
        res[lvl] += [walk.val]
        if walk.left :
            self.doit(res, walk.left, lvl+1 )
        if walk.right :
            self.doit(res, walk.right, lvl+1 )