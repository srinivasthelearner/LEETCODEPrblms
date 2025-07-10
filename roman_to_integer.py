# roman_to_integer.py

"""
LeetCode Problem: 13. Roman to Integer  
Link: https://leetcode.com/problems/roman-to-integer/

Approach:
- Create a dictionary to map Roman numerals to their integer values.
- Traverse the string in reverse order.
- If the current symbol is less than the previous one, subtract it.
- Otherwise, add it.
- This logic correctly handles subtraction cases like IV (4), IX (9), etc.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        previous = 0

        for char in reversed(s):
            current = roman_values[char]
            if current < previous:
                total -= current
            else:
                total += current
            previous = current

        return total
