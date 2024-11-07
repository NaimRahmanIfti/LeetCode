class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        # for i in range(len(flowerbed)):
        #     previous_plot = (i == 0) or (flowerbed[i-1] == 0)
        #     next_plot = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
        #     if flowerbed[i] == 0 and previous_plot and next_plot :
        #         flowerbed[i] = 1
        #         n -= 1
        # return n <= 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0

flowerbed = [0,0,1,0,0]
n = 1
print(Solution().canPlaceFlowers(flowerbed, n))