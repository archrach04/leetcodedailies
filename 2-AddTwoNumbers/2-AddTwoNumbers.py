# Last updated: 4/23/2026, 9:26:04 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8
9        dummy=ListNode()
10        curr=dummy
11        carry=0
12        while l1 or l2 or carry:
13            v1=l1.val if l1 else 0
14            v2=l2.val if l2 else 0
15            val=v1+v2+carry
16            carry=val//10
17            val=val%10
18            curr.next=ListNode(val)
19            
20            curr=curr.next
21            l1=l1.next if l1 else None
22            l2=l2.next if l2 else None
23        return dummy.next
24            
25
26        