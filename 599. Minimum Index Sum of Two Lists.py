class Solution:
    def findRestaurant(self, list1, list2):
        new_list = []
        min_sum = float('inf')
        index_map = {restaurant: i for i, restaurant in enumerate(list1)}

        for j, restaurant in enumerate(list2):
            if restaurant in index_map:
                sum_index = index_map[restaurant] + j
                if sum_index < min_sum:
                    new_list = [restaurant]
                    min_sum = sum_index
                elif sum_index == min_sum:
                    new_list.append(restaurant)

        return new_list

list1 = ["Shogun","Piatti","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(Solution().findRestaurant(list1, list2))
