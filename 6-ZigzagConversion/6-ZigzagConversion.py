# Last updated: 3/28/2026, 12:55:51 AM
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        rows=[]
        for j in range(numRows):
            rows.append([])
        i=0
        d=1

        for char in s:
            rows[i].append(char)
            i+=d
            if i==0:
                d=1
            elif i==numRows-1:
                d=-1
        
        ret=""
        for row in rows:
            ret+="".join(row)
        
        return ret

        