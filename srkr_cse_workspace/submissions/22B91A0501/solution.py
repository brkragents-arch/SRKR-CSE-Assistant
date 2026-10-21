# Student: 22B91A0501
# Assignment 1: Maximum Product of Two Distinct Elements
nums = list(map(int, input().split()))
nums.sort()
print(max(nums[0] * nums[1], nums[-1] * nums[-2]))
