nums = [0, 2, 1, 5, 3, 4]
ans = nums

for i in range(len(nums)):
    ans[i] = nums[nums[i]]

print(ans)
