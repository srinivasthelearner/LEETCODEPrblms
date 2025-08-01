"""
LeetCode Problem: 27. Remove Element  
LeetCode Link: https://leetcode.com/problems/remove-element/

Approach:
- We are given an array `nums` and a value `val`.
- The task is to remove all instances of `val` in-place and return the new length `k`.
- The order of elements can be changed, and values beyond `k` do not matter.
- Use a pointer `k` to track the index where the next non-`val` element should be placed.
- Iterate through the array:
    - If the current element is not equal to `val`, assign it to `nums[k]` and increment `k`.
- Return `k` as the count of elements not equal to `val`.
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for placing next valid element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
