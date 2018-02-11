'''
Created on Feb 11, 2018

@author: grekz
'''

class E107_BinaryTreeLevelOrderTraversalII:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def dfs(res, lvl, root):
            if ( root == None ): return
            le = len(res)
            lvl += 1
            if ( le < lvl ) :
                res.insert(0, [])
                le+=1
            res[le - lvl].append(root.val)
            dfs(res, lvl, root.left)
            dfs(res, lvl, root.right)
        dfs(res, 0, root)
        return res
        