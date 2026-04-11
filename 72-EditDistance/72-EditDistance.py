# Last updated: 4/11/2026, 7:10:12 PM
1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        rows, cols = len(word2)+1, len(word1)+1
4        matrix = [[0 for _ in range(cols)] for _ in range(rows)]
5
6        for i in range(len(matrix[0])):
7            matrix[0][i]=i
8        for i in range(len(matrix)):
9            matrix[i][0]=i
10        for r in range(1,len(matrix)):
11            for c in range(1,len(matrix[0])):
12                if word1[c-1]==word2[r-1]:
13                    matrix[r][c]=matrix[r-1][c-1]
14                else:
15                    matrix[r][c]=min(matrix[r-1][c],matrix[r][c-1],matrix[r-1][c-1])+1
16        return matrix[len(word2)][len(word1)]