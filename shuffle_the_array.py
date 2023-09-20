class Solution:
    def shuffle(self, nums: list[int], amount: int) -> list[int]:
        #ans = [0] * len(nums)
        ans = []
        n = 0

        for i in range(amount):
            n += 1

            #ans[i * 2] = nums[i]
            #ans[i + n] = nums[i + amount]

            ans.append(nums[i])
            ans.append(nums[i + amount])

        return ans


a = Solution()

print(a.shuffle([2, 5, 1, 3, 4, 7], 3))
