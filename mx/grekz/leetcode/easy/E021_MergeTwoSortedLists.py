'''
Created on Jan 10, 2018

@author: grekz
'''
from mx.grekz.leetcode.helper import ListNode

class E021_MergeTwoSortedLists:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if( l1 == None ) : return l2
        if( l2 == None ) : return l1
        temp = ListNode(-1)
        walk = temp
        while(l1 != None and l2 != None) :
            if(l1.val < l2.val):
                walk.next = l1
                l1 = l1.next
            else:
                walk.next = l2
                l2 = l2.next
            walk = walk.next
        if(l1 == None) :
            walk.next = l2
        if(l2 == None) :
            walk.next = l1
        return temp.next