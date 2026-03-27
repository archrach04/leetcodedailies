# Last updated: 3/28/2026, 12:55:31 AM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr=s.split()
        return len(arr[-1])
        