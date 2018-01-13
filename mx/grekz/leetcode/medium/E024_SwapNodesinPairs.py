'''
Created on Jan 13, 2018

@author: grekz
'''
from mx.grekz.leetcode.helper import ListNode

class E024_SwapNodesinPairs:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        res.next = head
        walk = res
        while ( walk.next != None and walk.next.next != None ) :
            a = walk.next
            b = walk.next.next
            a.next = b.next
            b.next = a
            walk.next = b
            walk = a
        return res.next