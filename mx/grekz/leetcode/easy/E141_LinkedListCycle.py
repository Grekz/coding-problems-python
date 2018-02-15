'''
Created on Feb 15, 2018

@author: grekz
'''

class E141_LinkedListCycle:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast) : return True
        return False