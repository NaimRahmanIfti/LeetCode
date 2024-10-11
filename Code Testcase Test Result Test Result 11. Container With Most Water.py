class Solution:
    def maxArea(self, height):
        n = len(height)
        left, right = 0, n - 1

        contain = 0
        while left < right:
            contain = max(contain, (right - left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return contain

height =[1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))