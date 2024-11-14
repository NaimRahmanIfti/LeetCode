class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        node = ListNode()
        node.next = head
        new_node = node
        current = head

        while current:
            next_node = current.next
            while next_node and current.val == next_node.val:
                next_node = next_node.next

            if current.next != next_node:
                new_node.next = next_node

            else:
                new_node = current
            current = next_node
        return node.next

head = [1,1,1,2,3]
print(Solution().deleteDuplicates(head))










