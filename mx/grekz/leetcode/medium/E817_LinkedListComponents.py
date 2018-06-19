'''
@author: grekz
'''
class E817_LinkedListComponents:

    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        s, res = set(G), 0
        while head != None :
            if head.val in s and ( head.next == None or not head.next.val in s ) :
                res += 1
            head = head.next
        return res