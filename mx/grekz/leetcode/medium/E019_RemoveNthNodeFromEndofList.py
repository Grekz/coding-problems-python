'''
Created on Jan 6, 2018

@author: grekz
'''

class E019_RemoveNthNodeFromEndofList:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if(head is None or n < 1): 
            return head
        size = 0
        walk = head
        while(walk.next):
            size+=1
            walk = walk.next
        index = size - (n - 1)
        if(index < 1):
            head = head.next
            return head
        walk = head
        i = 0
        while(walk.next):
            i+=1
            if(i == index):
                walk.next = walk.next.next
                break
            walk = walk.next
        return head