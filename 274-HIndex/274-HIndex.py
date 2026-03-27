# Last updated: 3/28/2026, 12:54:48 AM
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        paper_counts=[0]*(len(citations)+1)
        maxr=float('-inf')
        for i in citations:
            if i>=len(citations):
                paper_counts[len(citations)]+=1
            else:
                paper_counts[i]+=1
        tot=0
        for i in range(len(paper_counts)-1,-1,-1):
            tot+=paper_counts[i]
            if tot>=i:
                return i
        return maxr
                        
                
        