"""
LeetCode Problem: 189. Rotate Array  
LeetCode Link: https://leetcode.com/problems/rotate-array/

Approach:
- Use the in-place reversal algorithm to rotate the array with O(1) extra space.
- First, reverse the entire array.
- Then, reverse the first k elements.
- Finally, reverse the remaining n - k elements.
- This results in the array being rotated k steps to the right.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # In case k is larger than n

        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        reverse(0, n - 1)
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the rest
        reverse(k, n - 1)
