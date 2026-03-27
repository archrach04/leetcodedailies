# Last updated: 3/28/2026, 12:54:16 AM
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count=0
        for i in range(len(arr)):
            if arr[i]%2!=0:
                count+=1
            else:
                count=0
            if count==3:
                return True
        
        return False

        