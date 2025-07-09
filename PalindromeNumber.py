"""
LeetCode Problem: 9. Palindrome Number
LeetCode Link: https://leetcode.com/problems/palindrome-number/

Approach:
- A number is a palindrome if it reads the same forward and backward.
- Negative numbers are not palindromes due to the minus sign.
- Any number ending with 0 (except 0 itself) cannot be a palindrome.
- Reverse the second half of the number and compare with the first half.
- If they match (or the reversed part without the middle digit in case of odd length), it is a palindrome.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //= 10

        return x == reverse or x == reverse // 10
