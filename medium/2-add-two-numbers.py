"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # basic version that works
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_number_from_list_node(l: ListNode) -> int:
            digits: str = ""
            while l.next:
                digits += (str(l.val))
                l = l.next
            digits += (str(l.val))

            return int(digits[::-1])

        def convert_number_to_list_node(num: int) -> ListNode:
            digits: str = str(num)[::-1]
            head = None
            n = None
            for digit in digits:
                if head is None:
                    head = ListNode(int(digit))
                    n = head
                else:
                    n.next = ListNode(int(digit))
                    n = n.next

            return head

        num_1: int = get_number_from_list_node(l1)
        num_2: int = get_number_from_list_node(l2)

        num: int = num_1 + num_2

        return convert_number_to_list_node(num)

