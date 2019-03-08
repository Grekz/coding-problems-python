'''
@author: grekz
'''
class E143_ReorderList:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if ( head == None or head.next == None) : 
            return
        # // get to the middle, reverse second part, mix parts
        slow, fast = head, head
        while ( fast.next != None and fast.next.next != None ):
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        while (fast.next != None) :
            cur = fast.next
            fast.next = cur.next
            cur.next = slow.next
            slow.next = cur
        fast = slow.next
        cur = slow
        slow = head
        while ( slow != cur ) :
            cur.next = fast.next
            fast.next = slow.next
            slow.next = fast
            slow = fast.next
            fast = cur.next