'''
@author: grekz
'''
class E257_BinaryTreePaths:

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def traverse(node, cur) :
            cur = cur + str(node.val)
            if not node.left and not node.right :
                res.append(cur)
            else:
                if node.left :
                    traverse(node.left, cur + "->")
                if node.right:
                    traverse(node.right, cur + "->")
        if root :
            traverse(root, "")
        return res