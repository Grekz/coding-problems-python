'''
Created on Jan 15, 2018

@author: grekz
'''
from mx.grekz.leetcode.helper import ListNode
class MyClass:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge(lists, ini, las) :
            if ( ini > las ) : return None
            if ( ini == las ) : return lists[ini]
            mid = ( ini + las ) // 2
            a = merge(lists, ini, mid)
            b = merge(lists, mid+1, las)
            tmp = ListNode(0)
            cur = tmp
            while ( a != None and b != None ) :
                if ( a.val < b.val ) :
                    cur.next = a
                    a = a.next
                else:
                    cur.next = b
                    b = b.next               
                cur = cur.next
            cur.next = a if a != None else b
            return tmp.next
        return merge( lists, 0, len(lists) - 1 )
