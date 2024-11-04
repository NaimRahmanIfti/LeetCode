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
            if l1:
                l1.val = l1.val + carry
            if l2:
                l2.val = l2.val + carry
            sum = l1.val + l2.val 
            carry = sum // 10
            list.next = ListNode(sum % 10)
            list = list.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return list.next



l1 = [2,4,3]
l2 = [5,6,4]
s = Solution()
print(s.addTwoNumbers(l1, l2))






