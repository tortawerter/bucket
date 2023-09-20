nums = [1]
ans = [0] * len(nums) * 2
for i in range(len(nums)):
    ans[i], ans[i + len(nums)] = nums[i], nums[i]
print(ans)
