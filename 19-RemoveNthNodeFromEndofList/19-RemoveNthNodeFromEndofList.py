# Last updated: 8/1/2026, 8:43:58 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head, n):
8        dummy=ListNode(0)
9        dummy.next=head
10
11        fast=slow=dummy
12
13        for i in range(n):
14            fast=fast.next
15
16        while fast.next:
17            fast=fast.next
18            slow=slow.next
19        
20        slow.next=slow.next.next
21        
22        return dummy.next