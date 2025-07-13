"""
LeetCode Problem: 7. Reverse Integer  
LeetCode Link: https://leetcode.com/problems/reverse-integer/

Approach:
- Extract digits from the integer one by one using modulus (%) and integer division (//).
- Build the reversed number step by step.
- Handle negative numbers by preserving the sign.
- Check for 32-bit overflow on every step:
  - If the reversed number goes beyond [-2^31, 2^31 - 1], return 0.
"""

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow before updating rev
            if rev > (INT_MAX - digit) // 10:
                return 0

            rev = rev * 10 + digit

        return sign * rev
