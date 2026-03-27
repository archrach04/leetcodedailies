# Last updated: 3/28/2026, 12:55:32 AM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        res=[intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1]>=intervals[i][0]:
                last=res.pop()
                merged=[last[0],max(last[1],intervals[i][1])]
                res.append(merged)
            else:
                res.append(intervals[i])
        
        return res




