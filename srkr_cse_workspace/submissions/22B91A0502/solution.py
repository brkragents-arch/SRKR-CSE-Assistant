# Student: 22B91A0502
# Assignment 1: Maximum Product of Two Distinct Elements
nums = list(map(int, input().split()))
# Flawed logic: only multiplies first two elements instead of finding maximum product
print(nums[0] * nums[1])
