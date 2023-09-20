class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        sum_left = 0
        sum_right = 0
        ans = []

        for number in range(len(nums)):

            for number_left in range(0, number):
                if number_left != number:
                    sum_left += nums[number_left]

            for number_right in range(number, len(nums)):
                if number_right != number:
                    sum_right += nums[number_right]

            ans.append(abs(sum_left - sum_right))

            sum_left -= sum_left
            sum_right -= sum_right

        return ans


a = Solution()

print(a.leftRightDifference([1, 1, 1, 1]))
