class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        ans = 0
        for i in range(len(operations)):
            if operations[i] == "C++" or operations[i] == "++C":
                ans += 1
            elif operations[i] == "C--" or operations[i] == "--C":
                ans -=1
        return ans 


a = Solution()

print(a.finalValueAfterOperations(["--C", "C++", "C++"]))
