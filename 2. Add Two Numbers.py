class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        sum = []
        for i in reversed(l1):
            print(i)
            for j in reversed(l2):
                print(j)

        sum.append(i+ j)

        return sum
l1 = [2, 4, 3]
l2 = [5, 6, 4]
print(Solution().addTwoNumbers(l1, l2))
