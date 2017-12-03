'''
Created on Dec 3, 2017

@author: grekz
'''
from mx.grekz.leetcode.helper import ListNode

class E002_AddTwoNumbers:   
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = res = ListNode(-1)
        carry = 0
        while l1 or l2 or carry :
            sum = carry
            if l1 :
                sum += l1.val
                l1 = l1.next
            if l2 :
                sum += l2.val
                l2 = l2.next
            if sum > 9 :
                sum -= 10
                carry = 1
            else:
                carry = 0
            res.next = ListNode(sum)
            res = res.next
        return head.next