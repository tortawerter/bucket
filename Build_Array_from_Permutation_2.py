class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = nums.copy()

        for i in range(len(nums)):
            ans[i] = nums[nums[i]]

        return ans


a = Solution()

print(a.buildArray([0, 2, 1, 5, 3, 4]))
