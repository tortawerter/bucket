class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        first_num = n

        for i in range(151):
            if n % 2 == 0 and n % first_num == 0:
                break
            n += n

        return n


ans = Solution()

print(ans.smallestEvenMultiple(133))
