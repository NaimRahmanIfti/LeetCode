class Solution:
    def lemonadeChange(self, bills):
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                if five >0 and ten >0:
                    five -= 1
                    ten -= 1
            else:
                five -= 1
                ten -= 1
                if five >0 and ten >0:
                    five -= 1
                    ten -= 1
                elif five >0 and ten >0:



