'''
Created on Jan 31, 2018

@author: grekz
'''

class E083_RemoveDuplicatesfromSortedList:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None or head.next == None ):
            return head
        walk = head
        while(walk.next != None):
            curVal = walk.val
            if(curVal == walk.next.val):
                walk.next = walk.next.next
            else:
                walk = walk.next
        return head