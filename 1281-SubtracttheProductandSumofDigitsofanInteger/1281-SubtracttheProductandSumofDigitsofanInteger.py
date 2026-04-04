# Last updated: 4/5/2026, 1:10:22 AM
1class Solution:
2    def subtractProductAndSum(self, n: int) -> int:
3        prod=1
4        s=0
5        while n>0:
6            prod*=n%10
7            s+=n%10
8            n=n//10
9        return prod-s
10        