"""
LeetCode Problem: 58. Length of Last Word  
LeetCode Link: https://leetcode.com/problems/length-of-last-word/

Approach:
- Strip the input string to remove leading and trailing spaces.
- Split the stripped string into a list of words using default whitespace separator.
- The last element in this list is the last word.
- Return the length of this last word.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        return len(words[-1])
