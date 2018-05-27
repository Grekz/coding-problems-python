'''
@author: grekz
'''
class E328_OddEvenLinkedList:

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next and head.next.next :
            od, ev, evHe = head, head.next, head.next
            while ev and ev.next :
                od.next = od.next.next
                ev.next = ev.next.next
                od = od.next
                ev = ev.next
            od.next = evHe
        return head