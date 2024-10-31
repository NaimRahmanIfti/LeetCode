# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):

        list = ListNode()
        carry = 0
        while l1 or l2 is not None or carry != 0:
            l1.val = l1.val if l1 else 0
            l2.val = l2.val if l2 else 0
            sum = l1.val + l2.val + carry
            carry = sum // 10
            list.next = ListNode(sum % 10)
            list = list.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return list.next



l1 = ListNode([2,4,3])
l2 = ListNode([5,6,4])
s = Solution()
print(s.addTwoNumbers(l1, l2))






