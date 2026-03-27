# Last updated: 3/28/2026, 12:55:37 AM
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag=defaultdict(list)
        for word in strs:
            freq=[0]*26
            for c in word:
                freq[ord(c)-ord('a')]+=1
                
            key=tuple(freq)
            anag[key].append(word)
        return list(anag.values())
        