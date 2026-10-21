# Student: 22B91A0503
# Assignment 1: Maximum Product of Two Distinct Elements
nums = [int(x) for x in input().split()]
max_prod = float('-inf')
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] * nums[j] > max_prod:
            max_prod = nums[i] * nums[j]
print(max_prod)
