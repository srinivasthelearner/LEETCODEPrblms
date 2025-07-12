"""
LeetCode Problem: 14. Longest Common Prefix  
LeetCode Link: https://leetcode.com/problems/longest-common-prefix/

Approach:
- Assume the first string in the array is the potential longest common prefix.
- Compare this prefix with each of the remaining strings:
  - While the current string does not start with the prefix, remove the last character from the prefix.
  - Repeat until either the prefix matches the start of the current string or becomes empty.
- Return the final prefix after all comparisons.
- If the prefix becomes empty at any point, return "".
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
