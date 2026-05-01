# Last updated: 5/1/2026, 10:57:42 PM
1class Solution:
2    def removeStars(self, s: str) -> str:
3        st=[]
4        word=""
5        for i in range(len(s)):
6            if s[i]=="*":
7                st.pop()
8            else:
9                st.append(s[i])
10        for i in st:
11            word+=i
12        
13        return word
14
15        