# Last updated: 3/28/2026, 12:53:51 AM
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        numofemp=0
        for i in hours:
            if i>=target:
                numofemp+=1
        return numofemp
        
        