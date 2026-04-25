# Last updated: 4/25/2026, 10:39:51 PM
1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        hashm={}
4        used_words=set()
5        words=s.split()
6        if len(pattern) != len(words):
7            return False
8        for i in range(len(words)):
9            if pattern[i] in hashm:
10                if hashm[pattern[i]]==words[i]:
11                    continue
12                else:
13                    return False
14            else:
15                if words[i] not in used_words:
16                    hashm[pattern[i]]=words[i]
17                    used_words.add(words[i])
18                else:
19                    return False
20        return True
21        
22
23
24        