"""
LeetCode Problem: 2. Add Two Numbers  
LeetCode Link: https://leetcode.com/problems/add-two-numbers/

Approach:
- Use a dummy node to build the resulting linked list.
- Traverse both l1 and l2 simultaneously.
- At each step, add values from both nodes and any carry from the previous addition.
- Store (val1 + val2 + carry) % 10 as the new node's value.
- Carry forward the quotient (val1 + val2 + carry) // 10.
- Continue until both lists and carry are exhausted.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
