# Last updated: 4/19/2026, 11:21:24 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7
8    def rotateRight(self, head: ListNode, k: int) -> ListNode:
9        if not head:
10            return head
11
12    
13        length, tail = 1, head
14        while tail.next:
15            tail = tail.next
16            length += 1
17
18        k = k % length
19        if k == 0:
20            return head
21
22        cur = head
23        for i in range(length - k - 1):
24            cur = cur.next
25
26        newHead = cur.next
27        cur.next = None
28        tail.next = head
29
30        return newHead