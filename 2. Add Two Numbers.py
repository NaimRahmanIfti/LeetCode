class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0
        sum = 0
        while l1 or l2 or carry:
            if l1 is not None:
                sum += l1.val
                l1.val = l1.next
            if l2 is not None:
                sum += l2.val
                l2.val = l2.next
            sum += carry
            carry = sum // 10
            sum = sum % 10
            current.next = ListNode(sum)
            current = current.next
        return dummy.next

l1 = [2, 4, 3]
l2 = [5, 6, 4]
print(Solution().addTwoNumbers(l1, l2))
