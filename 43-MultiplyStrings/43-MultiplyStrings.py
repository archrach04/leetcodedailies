# Last updated: 4/2/2026, 11:02:24 PM
1class Solution:
2    def multiply(self, num1: str, num2: str) -> str:
3        if num1=="0" or num2=="0":
4            return "0"
5        n=len(num1)
6        m=len(num2)
7        res=[0]*(n+m)
8        for i in range(n-1,-1,-1):
9            for j in range(m-1,-1,-1):
10                mul=int(num1[i])*int(num2[j])
11
12                curr=i+j+1
13                carr=i+j
14
15                tot=res[curr]+mul
16                res[curr]=tot%10
17                res[carr]+=tot//10
18        result=[]
19        for nums in res:
20            if not (nums==0 and len(result)==0):
21                result.append(str(nums))
22        return ''.join(result)
23
24
25        