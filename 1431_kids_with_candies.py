class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        ans = []

        for amount in range(len(candies)):
            if candies[amount] + extraCandies >= max(candies):
                ans.append(True)
            else:
                ans.append(False)

        return ans


a = Solution()

print(a.kidsWithCandies([4, 2, 1, 1, 2], 1))
