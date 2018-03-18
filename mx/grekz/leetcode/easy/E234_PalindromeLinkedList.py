'''
@author: grekz
'''
class E234_PalindromeLinkedList:

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if(not head or not head.next) : return True
        if(not head.next.next) : return head.next.val == head.val
        fast = slow = head
        rev = None
        while ( fast and fast.next ) :
            fast = fast.next.next
            tmp = rev
            rev = slow
            slow = slow.next
            rev.next = tmp
        if ( fast ) :
            slow = slow.next;
        while ( rev and rev.val == slow.val ) :
            rev, slow = rev.next, slow.next
        return rev == None