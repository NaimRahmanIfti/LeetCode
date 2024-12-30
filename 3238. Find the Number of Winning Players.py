
class Solution:
    def winningPlayerCount(self, n, pick):
        win = []

        for i in range(n):
            for i in range(len(pick) - 1):
                for j in range (len(pick)):
                    if pick[i][j] == pick[i +1][j]:
                        win.append(pick[i][j])
                        pick[i] = pick[i+1]
                return len(win)
n = 4
pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
print(Solution().winningPlayerCount(n, pick))
