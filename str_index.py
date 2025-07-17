"""
LeetCode Problem: 28. Find the Index of the First Occurrence in a String  
LeetCode Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Approach:
- Slide a window of length len(needle) over haystack.
- Compare each substring with needle.
- Return the index as soon as a match is found.
- If no match is found, return -1.

Time Complexity: O(n * m) worst case  
Space Complexity: O(1)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i

        return -1
