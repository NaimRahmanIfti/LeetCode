class Solution:
        def longestConsecutive(self, nums):
            if not nums:
                return 0

            nums_set = set(nums)
            longest = 0

            for i in nums:
                if i - 1 not in nums_set:
                    current_num = i
                    length = 1

                    while current_num + 1 in nums_set:
                        current_num += 1
                        length += 1
                        nums_set.discard(current_num)
                        # print(length)
                    longest = max(longest, length)
                    # print(longest)

            return longest


nums = [100, 4, 200, 1, 3]
print(Solution().longestConsecutive())
