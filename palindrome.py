"""
LeetCode Problem: 125. Valid Palindrome  
LeetCode Link: https://leetcode.com/problems/valid-palindrome/

Approach:
- Use two pointers (left and right) to traverse from both ends.
- Skip any non-alphanumeric characters.
- Compare characters at left and right after converting to lowercase.
- If at any point they don’t match, return False.
- If pointers cross each other without mismatch, return True.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer to next alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer to previous alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
