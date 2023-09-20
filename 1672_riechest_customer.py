class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_ans = 0

        for amount in accounts:
            res = sum(amount)
            max_ans = max(res, max_ans)
        return max_ans


a = Solution()

print(a.maximumWealth([[15, 2, 3], [10, 2, 1]]))
