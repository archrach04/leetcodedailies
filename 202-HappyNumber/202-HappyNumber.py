# Last updated: 4/18/2026, 11:38:32 PM
1class Solution:
2    def isHappy(self, n: int) -> bool:
3        seen=set()
4
5        while n not in seen:
6            seen.add(n)
7            new=0
8            while n>0:
9                new+=(n%10)**2
10                n=n//10
11            n=new
12            if new==1:
13                return True
14
15        
16
17
18        return False
19
20
21        