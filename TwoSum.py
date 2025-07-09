"""
LeetCode Problem: 1. Two Sum
Link: https://leetcode.com/problems/two-sum/

Approach:
- We are given an array of integers (`nums`) and a target sum (`target`).
- The goal is to return the indices of the two numbers that add up to the target.
- We use a hash map (`seen`) to store the number and its index as we iterate.
- For each element, calculate its complement (target - current number).
- If the complement is already in the map, we return the pair of indices.
- This approach runs in O(n) time with O(n) space.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Dictionary to store value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
