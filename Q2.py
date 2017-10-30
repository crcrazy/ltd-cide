# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    @staticmethod
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        outcome=ListNode(0)
        value=0
        p=outcome
        while l1 or l2:
            value=carry
            carry=0
            if l1:
                value=value+l1.val
                l1=l1.next
            if l2:
                value=value+l2.val
                l2=l2.next
            carry=value/10
            value=value%10
            p.next=ListNode(value)
        if carry <>0: p.next=ListNode(carry)
        return outcome.next
L1=[1,2,3]
L2=[4,5,6]
print Solution.addTwoNumbers(L1,L2)