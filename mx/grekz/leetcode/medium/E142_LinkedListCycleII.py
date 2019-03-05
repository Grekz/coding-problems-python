'''
@author: grekz
'''
class E142_LinkedListCycleII:

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next :
            slow, fast = slow.next, fast.next.next
            if fast == slow :
                slow = head
                while slow != fast :
                    slow, fast = slow.next, fast.next
                return slow          
        return None