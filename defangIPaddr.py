class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for i in range(len(address)):
            if address[i] == ".":
                ans += "[.]"
            else:
                ans += address[i]
        return ans

solution = Solution()

print(solution.defangIPaddr("1.1.25.1.1"))