# Last updated: 4/28/2026, 1:14:28 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if head is None or head.next is None:
9            return head
10        odd=head
11        even=even_head=head.next
12
13        while even and even.next:
14            odd.next=even.next
15            odd=odd.next
16            even.next=odd.next
17            even=even.next
18        odd.next=even_head
19        return head
20
21
22        