class Solution:
    def minimizedStringLength(self, s: str) -> int:
        ans = ""
        output = ""
        
        for i in range(len(s)):
            if s[i] in ans:
                pass
            else:
                output += s[i]
            ans += s[i]
            
        return len(output)

        
a = Solution()

print(a.minimizedStringLength("ipi"))
