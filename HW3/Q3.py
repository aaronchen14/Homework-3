# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Modify the “solution” class in question3.py, you may design your input to test it.

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        copy = ListNode(0)
        l3 = copy
        carry = 0
        while l1 is not None or l2 is not None:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0

            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            total = l1_val + l2_val + carry
            carry = total * 10

            l3.next = ListNode(carry/10)
            l3 = l3.next

            if l1:
                l1 = l1.next
            else:
                l1 = None

            if l2:
                l2 = l2.next
            else:
                l2 = None
        if carry > 0:
            # print(l3.val)
            l3.next = ListNode(carry)

        return l3.val #copy.next


l1_input1 = ListNode(2)
l1_input2 = ListNode(4)
l1_input3 = ListNode(3)
l1_input1.next = l1_input2
l1_input2.next = l1_input3


l2_input1 = ListNode(5)
l2_input2 = ListNode(6)
l2_input3 = ListNode(4)
l2_input1.next = l2_input2
l2_input2.next = l2_input3

outcome = Solution().addTwoNumbers(l1_input1, l2_input1)
print(outcome)

