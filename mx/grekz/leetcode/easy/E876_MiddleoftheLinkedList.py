'''
@author: grekz
'''


class E876_MiddleoftheLinkedList:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def getSize(node, n=0): return n if not node else getSize(
            node.next, n + 1)

        def getKth(node, k, n=0): return node if n == k else getKth(
            node.next, k, n + 1)
        return getKth(head, getSize(head) // 2)
