"""
LeetCode Problem: 21. Merge Two Sorted Lists  
LeetCode Link: https://leetcode.com/problems/merge-two-sorted-lists/

Approach:
- Use a dummy node to simplify the process of building the merged list.
- Use a pointer (`current`) to track the last node in the merged list.
- Compare the nodes of list1 and list2:
  - Append the smaller node to the merged list.
  - Move the pointer in that list forward.
- Once one list is exhausted, connect the remaining part of the other list.
- Return `dummy.next` as the head of the merged list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Connect the remaining part of the list
        current.next = list1 if list1 else list2

        return dummy.next
