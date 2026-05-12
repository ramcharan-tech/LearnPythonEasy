# File: /Blind75/Blind75/problems/01_two_sum.py

"""
Problem Statement:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Hints:
1. Consider using a hash map to store the indices of the numbers you have seen so far.
2. As you iterate through the list, check if the complement (target - current number) exists in the hash map.
3. If it does, you have found the two indices you need.

Solution:
"""

def two_sum(nums, target):
    num_to_index = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    
    return []  # In case there is no solution, though the problem guarantees one.