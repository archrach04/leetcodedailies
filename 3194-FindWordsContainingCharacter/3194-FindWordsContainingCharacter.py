# Last updated: 3/28/2026, 12:53:50 AM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        op=[]
        for i in range(len(words)):
            for j in words[i]:
                if j==x:
                    op.append(i)
                    break
                
        return op