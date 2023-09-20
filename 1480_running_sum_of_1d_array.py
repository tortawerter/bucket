from typing import List


class Solution:
    def runningSun(self, nums: List[int]) -> List[int]:
        ans = 0
        output = []

        for amount in nums:
            ans += amount
            output.append(ans)

        return output


a = Solution()

print(a.runningSun([1, 1, 1, 1, 1]))
