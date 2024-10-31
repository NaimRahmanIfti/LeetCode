# class Solution:
#     def maximumSwap(self, num):
#         count = 0
#         l = []
#         for i in num:
#             l.append(i)
#         for j in range(num):
#             if num[j] < num[j+1]:
#                 num[j] = num[j+1]
#                 count += 1
#         return count
#
# s = Solution()
# print(s.maximumSwap())

num = 2763
count = 0
list = [num]
for i in list:
    if list[i] < list[i+1]:
        count += 1

print(count)