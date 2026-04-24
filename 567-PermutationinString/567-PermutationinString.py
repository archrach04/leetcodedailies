# Last updated: 4/24/2026, 6:40:54 PM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        if len(s1) > len(s2):
4            return False
5        count_1=[0]*26
6        count_2=[0]*26
7        for i in s1:
8            count_1[ord(i)-97]+=1
9        l=0
10        r=len(s1)
11        for i in range(l,r):
12            count_2[ord(s2[i])-97]+=1
13
14        while r<=len(s2):
15            if count_2==count_1:
16                return True
17            if r==len(s2):
18                break
19            count_2[ord(s2[l])-97]-=1
20            count_2[ord(s2[r])-97]+=1
21            l+=1
22            r+=1
23        return False
24
25        