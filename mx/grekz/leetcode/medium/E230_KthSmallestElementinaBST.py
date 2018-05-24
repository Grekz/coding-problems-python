'''
@author: grekz
'''
class E230_KthSmallestElementinaBST:

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = self.countit(root.left) + 1
        if count == k : return root.val
        if k > count : return self.kthSmallest(root.right, k - count)
        return self.kthSmallest(root.left, k)
        
    def countit(self, n):
        if not n : return 0
        return 1 + self.countit(n.left) + self.countit(n.right)