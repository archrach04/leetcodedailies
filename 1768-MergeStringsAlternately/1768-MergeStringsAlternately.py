# Last updated: 4/30/2026, 10:46:56 PM
1class Solution:
2    def uniqueOccurrences(self, arr: List[int]) -> bool:
3        hashm={}
4        s=set()
5        for i in arr:
6            if i in hashm:
7                hashm[i]+=1
8            else:
9                hashm[i]=1
10        for i in hashm:
11            if hashm[i] in s:
12                return False
13            else:
14                s.add(hashm[i])
15        
16        return True
17
18        