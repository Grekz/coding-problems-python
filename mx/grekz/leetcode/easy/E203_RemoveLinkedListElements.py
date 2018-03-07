'''
Created on Mar 7, 2018

@author: grekz
'''
from mx.grekz.leetcode.helper import ListNode

class E203_RemoveLinkedListElements:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None : return head
        fh = ListNode(-1)
        cur = fh
        fh.next = head
        while cur.next != None :
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return fh.next