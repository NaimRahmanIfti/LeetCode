class Solution:
    def winningPlayerCount(self, n, pick):

        win = []

        for i in range(len(pick) - 1):
            if pick[i] == pick[i+1]:
                win.append(i)
                pick[i] = pick[i+1]

            return len(win)




n = 4
pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
print(Solution().winningPlayerCount(n, pick))
