# Last updated: 5/2/2026, 11:52:41 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val, prev, next, child):
5        self.val = val
6        self.prev = prev
7        self.next = next
8        self.child = child
9"""
10
11class Solution:
12    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
13        if not head:
14            return head
15        node=head
16
17        while node:
18            if not node.child:
19                node=node.next
20            else:
21                nextNode=node.next
22                node.next=node.child
23                node.child.prev=node
24
25                temp=node.child
26                while temp.next:
27                    temp=temp.next
28                temp.next=nextNode
29                if nextNode:
30                    nextNode.prev=temp
31                node.child=None
32                node=node.next
33        
34        return head