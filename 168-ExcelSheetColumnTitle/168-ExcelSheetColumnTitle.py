# Last updated: 5/7/2026, 1:33:26 AM
1class Solution:
2    def convertToTitle(self, columnNumber: int) -> str:
3        word = ""
4        while columnNumber:
5            n = (columnNumber - 1) % 26
6            word += chr(n + 65)
7            columnNumber = (columnNumber - 1) // 26
8        return word[::-1]