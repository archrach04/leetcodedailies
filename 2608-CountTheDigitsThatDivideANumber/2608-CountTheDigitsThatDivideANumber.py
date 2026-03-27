# Last updated: 3/28/2026, 12:53:54 AM
class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        numnew=num
        while numnew>0:
            div=numnew%10
            if num%div==0:
                count+=1
            numnew=numnew//10
        return count
        