'''
Created on Mar 17, 2018

@author: grekz
'''

class E237_DeleteNodeinaLinkedList(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next