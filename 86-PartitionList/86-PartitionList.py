# Last updated: 4/21/2026, 9:57:25 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
8        leftlist=ListNode()
9        rightlist=ListNode()
10
11        lefthead=leftlist
12        righthead=rightlist
13
14        while head:
15            if head.val>=x:
16                righthead.next=head
17                righthead=righthead.next
18            else:
19                lefthead.next=head
20                lefthead=lefthead.next
21            
22            head=head.next
23        
24        lefthead.next=rightlist.next
25        righthead.next=None
26        
27
28
29        return leftlist.next
30        