class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        max_ones = 0
        count_ones = -1

        for i, j in enumerate(mat):
            if max_ones < j.count(1):
                max_ones = j.count(1)
                count_ones = i

        return [count_ones, max_ones]


a = Solution()

print(a.rowAndMaximumOnes([[0, 0], [1, 1], [0, 0]]))
