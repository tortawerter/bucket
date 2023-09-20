class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ans = [0, 0]
        for i in range(len(moves)):
            if moves[i] == "U":
                ans[1] += 1
            elif moves[i] == "D":
                ans[1] -= 1
            elif moves[i] == "R":
                ans[0] += 1
            elif moves[i] == "L":
                ans[0] -= 1
        # return ans[0] == 0 and ans[1] == 0
        return ans == len(moves) * [0]


a = Solution()

print(a.judgeCircle("LL"))



