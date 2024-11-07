# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2, val=0 ) -> [ListNode]:
        self.val = val
        head = ListNode()
        current = head
        if current is None:
            return current
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        current.next = list1 or list2
        return head.next
list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(Solution().mergeTwoLists(list1, list2))