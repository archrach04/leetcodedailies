# Last updated: 4/6/2026, 11:47:49 PM
1class Solution:
2    def reverse(self, x: int) -> int:
3        x=str(x)
4        num=''
5        neg=0
6        if x[0]=='-':
7            neg=1
8            x=x[1:]
9        for i in range(len(x)-1,-1,-1):
10            num+=x[i]
11        if neg==1:
12            num='-'+num
13        if -2**31<int(num)<2**(31)-1:
14            return int(num)
15        else:
16            return 0
17        
18
19
20        