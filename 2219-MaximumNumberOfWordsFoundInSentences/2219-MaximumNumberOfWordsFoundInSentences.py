# Last updated: 3/28/2026, 12:53:59 AM
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxw=float('-inf')
        for i in range(len(sentences)):
            maxw=max(maxw,len(sentences[i].split()))
        
        return maxw
        