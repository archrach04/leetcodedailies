# Last updated: 5/10/2026, 10:11:18 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        row=len(grid)
4        column=len(grid[0])
5        tot=0
6        def dfs(i,j):
7            if i<0 or i>=row or j<0 or j>=column or grid[i][j]!='1':
8                return
9            else:
10                grid[i][j]='0'
11                dfs(i,j+1)
12                dfs(i+1,j)
13                dfs(i-1,j)
14                dfs(i,j-1)
15
16
17        for i in range(row):
18            for j in range(column):
19                if grid[i][j]=='1':
20                    tot+=1
21                    dfs(i,j)
22        
23        return tot
24        