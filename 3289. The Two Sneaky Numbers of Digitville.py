nums = [0,1,1,0]
new = [i for i in set(nums) if nums.count(i) > 1]
# new = [i for i in set(nums) if nums.count(i) > 1]
# for i in set(nums):
#     print(i)
#     if nums.count(i) > 1:
#         new.append(i)
print(new)