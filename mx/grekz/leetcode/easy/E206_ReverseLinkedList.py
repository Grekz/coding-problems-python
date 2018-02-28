'''
Created on Feb 28, 2018

@author: grekz
'''

class E206_ReverseLinkedList:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = res = None
        while(head!=None):
            cur = head
            head = head.next
            cur.next = res
            res = cur
        return res
        