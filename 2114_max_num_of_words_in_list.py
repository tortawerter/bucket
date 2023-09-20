from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = []

        for i in range(len(sentences)):
            ans.append(len(sentences[i].split()))
        return max(ans)


a = Solution()

print(a.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
