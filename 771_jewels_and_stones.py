class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        output = 0

        for stone in stones:
            if stone in jewels:
                output += 1
        return output


a = Solution()

print(a.numJewelsInStones("Zisfr", "ZFfZisss"))
