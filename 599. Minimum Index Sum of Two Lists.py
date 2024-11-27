class Solution:
    def findRestaurant(self, list1, list2):

        min_sum = float()
        new_l = []
        for i in range(len(list1)):``


            for j in range(len(list2)):
                if list2[j] in list1[i]:
                    index_sum = i + j
                    if index_sum < min_sum:
                        min_sum = index_sum
                        new_l = [list1[i], list2[j]]

                    elif index_sum == min_sum:
                        new_l.append(list2[j])
        return new_l


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(Solution().findRestaurant(list1, list2))
``