'''
Created on Feb 18, 2018

@author: grekz
'''

class E160_IntersectionofTwoLinkedLists:
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if(headA == None or headB == None) : return None
        a = headA
        b = headB
        while( a != b) :
            a = headB if a == None else a.next
            b = headA if b == None else b.next    
        return a
        